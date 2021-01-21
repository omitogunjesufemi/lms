from typing import List

from django.contrib.auth.models import User, Group

from lms_app.lms_dto.StudentDto import *
from abc import ABCMeta, abstractmethod

from lms_app.models import Student


class StudentRepository(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: RegisterStudentDto):
        """Register Student"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, student_id:int, model: EditStudentDto):
        """Edit Student"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListStudentDto]:
        """List Student"""
        raise NotImplementedError

    @abstractmethod
    def list_student_for_course(self, course_id) -> List[ListStudentDto]:
        """List Student"""
        raise NotImplementedError

    @abstractmethod
    def details(self, user_id: int) -> StudentDetailsDto:
        """Details of Student"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, student_id: int):
        """Delete Student"""
        raise NotImplementedError


class DjangoORMStudentRepository(StudentRepository):
    def register(self, model: RegisterStudentDto):

        check_user = User.objects.get(username=model.username)
        if check_user is None:
            student = Student()
            student.phone = model.phone
            student.registration_number = model.registration_number

            user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
            user.first_name = model.first_name
            user.last_name = model.last_name
            user.save()

            student.user = user
            students, create = Group.objects.get_or_create(name='students')
            user.groups.add(students)

            student.save()
            return student.id
        else:
            raise Exception


    def edit(self, student_id:int, model: EditStudentDto):
        try:
            student = Student.objects.get(id=student_id)
            student.user.first_name = model.first_name
            student.user.last_name = model.last_name
            student.user.email = model.email
            student.phone = model.phone
            student.user.username = model.username

            student.save()
            student.user.save()
        except Student.DoesNotExist as e:
            print('This Student does not exist!')
            raise e

    def list(self) -> List[ListStudentDto]:
        students = list(Student.objects.values('id',
                                               'user__first_name',
                                               'user__last_name',
                                               'user__username',
                                               'user__email',
                                               'registration_number',
                                               ))
        students_list: List[ListStudentDto] = []

        for student in students:
            learner = ListStudentDto()
            learner.id = student['id']
            learner.first_name = student['user__first_name']
            learner.last_name = student['user__last_name']
            learner.username = student['user__username']
            learner.email = student['user__email']
            learner.registration_number = student['registration_number']
            students_list.append(learner)

        return students_list

    def list_student_for_course(self, course_id) -> List[ListStudentDto]:
        students = list(Student.objects.values('id',
                                               'user__first_name',
                                               'user__last_name',
                                               'user__username',
                                               'user__email',
                                               'registration_number',
                                               'user__student__course'
                                               ))
        students_list: List[ListStudentDto] = []

        for student in students:
            if course_id == student['user__student__course']:
                learner = ListStudentDto()
                learner.id = student['id']
                learner.first_name = student['user__first_name']
                learner.last_name = student['user__last_name']
                learner.username = student['user__username']
                learner.email = student['user__email']
                learner.registration_number = student['registration_number']
                students_list.append(learner)

        return students_list

    def details(self, user_id: int) -> StudentDetailsDto:
        try:
            student = Student.objects.get(user_id=user_id)
            student_details = StudentDetailsDto()
            student_details.id = student.id
            student_details.first_name = student.user.first_name
            student_details.last_name = student.user.last_name
            student_details.username = student.user.username
            student_details.email = student.user.email
            student_details.phone = student.phone
            student_details.registration_number = student.registration_number
            return student_details
        except Student.DoesNotExist as e:
            print('This Student was not found!')
            raise e

    def delete(self, student_id: int):
        try:
            student = Student.objects.get(id=student_id)
            user_id = student.user.id
            student.delete()
            User.objects.get(id=user_id).delete()
        except Student.DoesNotExist as e:
            print('This Student was not found!')
            raise e





