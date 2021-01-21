from abc import ABCMeta, abstractmethod
from typing import List

from lms.lms_app.lms_dto.ApplyDto import ApplyDto
from lms.lms_app.lms_repository.ApplyRepository import ApplyRepository


class ApplyManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: ApplyDto):
        """Apply as a tutor"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, apply_id, model: ApplyDto):
        """Update application"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ApplyDto]:
        """List Applications"""
        raise NotImplementedError


    def details(self, apply_id) -> ApplyDto:
        """Details of a particular application"""
        raise NotImplementedError

    def delete(self, apply_id):
        """Delete a comment"""
        raise NotImplementedError


class DefaultApplyManagementService(ApplyManagementService):
    repository = ApplyRepository

    def __init__(self, repository: ApplyRepository):
        self.repository = repository

    def register(self, model: ApplyDto):
        return self.repository.register(model)

    def edit(self, apply_id, model: ApplyDto):
        return self.repository.edit(apply_id, model)

    def list(self) -> List[ApplyDto]:
        return self.repository.list()

    def details(self, apply_id) -> ApplyDto:
        return self.repository.details(apply_id)

    def delete(self, apply_id):
        return self.repository.delete(apply_id)