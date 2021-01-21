from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import User, Group

from lms.lms_app.lms_dto.TutorDto import *
from lms.lms_app.models import Tutor


class TutorRepository(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: RegisterTutorDto):
        """Register Student"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, tutor_id: int, model: EditTutorDto):
        """Edit Tutor"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListTutorDto]:
        """List Tutors"""
        raise NotImplementedError

    @abstractmethod
    def details(self, user_id: int) -> TutorDetailsDto:
        """Details of Tutor"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, tutor_id: int):
        """Delete Tutor"""
        raise NotImplementedError


class DjangoORMTutorRepository(TutorRepository):
    def register(self, model: RegisterTutorDto):
        tutor = Tutor()
        tutor.phone = model.phone
        tutor.registration_number = model.registration_number

        user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()

        tutor.user = user
        tutors, create = Group.objects.get_or_create(name='tutors')
        user.groups.add(tutors)

        tutor.save()
        return tutor.id

    def edit(self, tutor_id: int, model: EditTutorDto):
        try:
            tutor = Tutor.objects.get(id=tutor_id)
            tutor.phone = model.phone
            tutor.user.first_name = model.first_name
            tutor.user.last_name = model.last_name
            tutor.user.username = model.username
            tutor.user.email = model.email

            tutor.save()
            tutor.user.save()
        except Tutor.DoesNotExist as e:
            print('This tutor does not exist!')
            raise e

    def list(self) -> List[ListTutorDto]:
        tutors = list(Tutor.objects.values('id',
                                           'user__first_name',
                                           'user__last_name',
                                           'user__email',
                                           'phone',
                                           'registration_number',
                                           ))
        tutors_list: List[ListTutorDto] = []

        for tutor in tutors:
            teacher = ListTutorDto()
            teacher.id = tutor['id']
            teacher.first_name = tutor['user__first_name']
            teacher.last_name = tutor['user__last_name']
            teacher.phone = tutor['phone']
            teacher.email = tutor['user__email']
            teacher.registration_number = tutor['registration_number']
            tutors_list.append(teacher)

        return tutors_list

    def details(self, user_id: int) -> TutorDetailsDto:
        try:
            tutor = Tutor.objects.get(user_id=user_id)
            tutor_details = TutorDetailsDto()
            tutor_details.id = tutor.id
            tutor_details.first_name = tutor.user.first_name
            tutor_details.last_name = tutor.user.last_name
            tutor_details.username = tutor.user.username
            tutor_details.email = tutor.user.email
            tutor_details.phone = tutor.phone
            tutor_details.registration_number = tutor.registration_number
            return tutor_details
        except Tutor.DoesNotExist as e:
            print('This tutor cannot be found!')
            raise e

    def delete(self, tutor_id: int):
        try:
            tutor = Tutor.objects.get(id=tutor_id)
            user_id = tutor.user.id
            tutor.delete()
            User.objects.get(id=user_id).delete()
        except Tutor.DoesNotExist as e:
            print('This tutor does not exist!')
            raise e
