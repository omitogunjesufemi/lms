from abc import abstractmethod, ABCMeta

from lms_app.lms_repository import AssessmentRepository
from lms_app.lms_repository.AssessmentRepository import *


class AssessmentManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: CreateAssessmentDto):
        """Create an assessment for a Registered Course"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, assessment_id, model: UpdateAssessmentDto):
        """Update an assessment for a Registered Course"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListAssessmentDto]:
        """List the assessments for a course"""
        raise NotImplementedError

    @abstractmethod
    def list_assessment_for_student(self, student_id) -> List[ListAssessmentDto]:
        """List the assessments for a course"""
        raise NotImplementedError

    @abstractmethod
    def list_assessment_for_tutor(self, tutor_id) -> List[ListAssessmentDto]:
        """List the assessments for a course"""
        raise NotImplementedError

    def details(self, assessment_id) -> AssessmentDetailsDto:
        """Details of a particular enrollment"""
        raise NotImplementedError

    def delete(self, assessment_id):
        """Delete an enrollment for a course"""
        raise NotImplementedError


class DefaultAssessmentManagementService(AssessmentManagementService):
    repository = AssessmentRepository

    def __init__(self, repository: AssessmentRepository):
        self.repository = repository

    def register(self, model: CreateAssessmentDto):
        return self.repository.register(model)

    def edit(self, assessment_id, model: UpdateAssessmentDto):
        return self.repository.edit(model)

    def list(self) -> List[ListAssessmentDto]:
        return self.repository.list()

    def list_assessment_for_student(self, student_id) -> List[ListAssessmentDto]:
        return self.repository.list_assessment_for_student(student_id)

    def list_assessment_for_tutor(self, tutor_id) -> List[ListAssessmentDto]:
        return self.repository.list_assessment_for_tutor(tutor_id)

    def details(self, assessment_id) -> AssessmentDetailsDto:
        return self.repository.details(assessment_id)

    def delete(self, assessment_id):
        return self.repository.delete(assessment_id)