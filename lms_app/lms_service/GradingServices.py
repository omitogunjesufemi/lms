from abc import abstractmethod, ABCMeta

from lms_app.lms_repository.GradingRepository import *


class GradingManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: GradeSittingDto):
        """Enroll a student for a Course"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, grading_id, model: GradeSittingDto):
        """Update a Student Registered Courses"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[GradeSittingDto]:
        """List the student and courses enrolled"""
        raise NotImplementedError

    def details(self, sitting_id) -> GradeSittingDto:
        """Details of a particular enrollment"""
        raise NotImplementedError

    def delete(self, grading_id):
        """Delete an enrollment for a course"""
        raise NotImplementedError


class DefaultGradingManagementService(GradingManagementService):
    repository = GradingRepository

    def __init__(self, repository: GradingRepository):
        self.repository = repository

    def register(self, model: GradeSittingDto):
        return self.repository.register(model)

    def edit(self, grading_id, model: GradeSittingDto):
        return self.repository.edit(grading_id, model)

    def list(self) -> List[GradeSittingDto]:
        return self.repository.list()

    def details(self, sitting_id) -> GradeSittingDto:
        return self.repository.details(sitting_id)

    def delete(self, grading_id):
        return self.repository.delete(grading_id)