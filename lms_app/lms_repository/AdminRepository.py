from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import User, Group

from lms_app.lms_dto.AdminDto import *
from lms_app.models import AdminUser


class AdminRepository(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: RegisterAdminDto):
        """Register Admin"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, admin_id: int, model: EditAdminDto):
        """Edit Tutor"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListAdminDto]:
        """List Tutors"""
        raise NotImplementedError

    @abstractmethod
    def details(self, user_id: int) -> AdminDetailsDto:
        """Details of Tutor"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, admin_id: int):
        """Delete Tutor"""
        raise NotImplementedError


class DjangoORMAdminRepository(AdminRepository):
    def register(self, model: RegisterAdminDto):
        admin = AdminUser()
        admin.phone = model.phone

        user = User.objects.create_superuser(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()

        admin.user = user
        admins, create = Group.objects.get_or_create(name='admin')
        user.groups.add(admins)

        admin.save()
        return admin.id

    def edit(self, admin_id: int, model: EditAdminDto):
        try:
            admin = AdminUser.objects.get(id=admin_id)
            admin.phone = model.phone
            admin.user.first_name = model.first_name
            admin.user.last_name = model.last_name
            admin.user.username = model.username
            admin.user.email = model.email

            admin.save()
            admin.user.save()
        except AdminUser.DoesNotExist as e:
            print('This admin does not exist!')
            raise e

    def list(self) -> List[ListAdminDto]:
        admins = list(AdminUser.objects.values('id',
                                               'user__first_name',
                                               'user__last_name',
                                               'user__email',
                                               'phone',
                                           ))
        admin_list: List[ListAdminDto] = []

        for admin in admins:
            adm = ListAdminDto()
            adm.id = admin['id']
            adm.first_name = admin['user__first_name']
            adm.last_name = admin['user__last_name']
            adm.phone = admin['phone']
            adm.email = admin['user__email']
            adm.registration_number = admin['registration_number']
            admin_list.append(adm)

        return admin_list

    def details(self, user_id: int) -> AdminDetailsDto:
        try:
            admin = AdminUser.objects.get(user_id=user_id)
            admin_details = AdminDetailsDto()
            admin_details.id = admin.id
            admin_details.first_name = admin.user.first_name
            admin_details.last_name = admin.user.last_name
            admin_details.username = admin.user.username
            admin_details.email = admin.user.email
            admin_details.phone = admin.phone
            return admin_details
        except AdminUser.DoesNotExist as e:
            print('This admin cannot be found!')
            raise e

    def delete(self, tutor_id: int):
        try:
            AdminUser.objects.get(id=tutor_id).delete()
        except AdminUser.DoesNotExist as e:
            print('This admin does not exist!')
            raise e
