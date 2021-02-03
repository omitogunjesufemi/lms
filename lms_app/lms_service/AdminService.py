from abc import abstractmethod, ABCMeta

from lms_app.lms_repository.AdminRepository import *


class AdminManagementService(metaclass=ABCMeta):
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


class DefaultAdminManagementService(AdminManagementService):
    repository = AdminRepository

    def __init__(self, repository: AdminRepository):
        self.repository = repository

    def register(self, model: RegisterAdminDto):
        return self.repository.register(model)

    def edit(self, admin_id: int, model: EditAdminDto):
        return self.repository.edit(admin_id, model)

    def list(self) -> List[ListAdminDto]:
        return self.repository.list()

    def details(self, user_id: int) -> AdminDetailsDto:
        return self.repository.details(user_id)

    def delete(self, admin_id: int):
        return self.repository.delete(admin_id)