from abc import abstractmethod, ABCMeta

from lms_app.lms_repository import SittingRepository
from lms_app.lms_repository.SittingRepository import *


class SittingManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: NewSittingDto):
        """Create an assessment for a Registered Course"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, sitting_id, model: RetakeSittingDto):
        """Update an assessment for a Registered Course"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListSittingDto]:
        """List the assessments for a course"""
        raise NotImplementedError

    @abstractmethod
    def list_of_sitting_for_student_assessment(self, student_id) -> List[ListSittingDto]:
        """List the assessments for a course"""
        raise NotImplementedError

    @abstractmethod
    def details(self, sitting_id) -> SittingDetailsDto:
        """Details of a particular enrollment"""
        raise NotImplementedError

    def delete(self, sitting_id):
        """Delete an enrollment for a course"""
        raise NotImplementedError


class DefaultSittingManagementService(SittingManagementService):
    repository = SittingRepository

    def __init__(self, repository: SittingRepository):
        self.repository = repository

    def register(self, model: NewSittingDto):
        return self.repository.register(model)

    def edit(self, sitting_id, model: RetakeSittingDto):
        return self.repository.edit(model)

    def list(self) -> List[ListSittingDto]:
        return self.repository.list()

    def list_of_sitting_for_student_assessment(self, student_id) -> List[ListSittingDto]:
        return self.repository.list_of_sitting_for_student_assessment(student_id=student_id)

    def details(self, sitting_id) -> SittingDetailsDto:
        return self.repository.details(sitting_id)

    def delete(self, sitting_id):
        return self.repository.delete(sitting_id)