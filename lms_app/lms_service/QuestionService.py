from abc import abstractmethod, ABCMeta

from lms_app.lms_repository import QuestionRepository
from lms_app.lms_repository.QuestionRepository import *


class QuestionManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: SetQuestionDto):
        """Create a question for an assessment"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, question_id, model: UpdateQuestionDto):
        """Update a question for an assessment"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListQuestionDto]:
        """List the question for an assessment"""
        raise NotImplementedError

    @abstractmethod
    def list_for_assessment(self, assessment_id) -> List[ListQuestionDto]:
        """List the question for an assessment"""
        raise NotImplementedError

    @abstractmethod
    def list_question_for_tutor(self, tutor_id) -> List[ListQuestionDto]:
        """List the question for an assessment"""
        raise NotImplementedError

    def details(self, question_id) -> GetQuestionDto:
        """Details of a question for an assessment"""
        raise NotImplementedError

    def delete(self, question_id):
        """Delete a question for an assessment"""
        raise NotImplementedError


class DefaultQuestionManagementService(QuestionManagementService):
    repository = QuestionRepository

    def __init__(self, repository: QuestionRepository):
        self.repository = repository

    def register(self, model: SetQuestionDto):
        return self.repository.register(model)

    def edit(self, question_id, model: UpdateQuestionDto):
        return self.repository.edit(question_id, model)

    def list(self) -> List[ListQuestionDto]:
        return self.repository.list()

    def list_for_assessment(self, assessment_id) -> List[ListQuestionDto]:
        return self.repository.list_for_assessment(assessment_id=assessment_id)

    def list_question_for_tutor(self, tutor_id) -> List[ListQuestionDto]:
        return self.repository.list_question_for_tutor(tutor_id)

    def details(self, question_id) -> GetQuestionDto:
        return self.repository.details(question_id)

    def delete(self, question_id):
        return self.repository.delete(question_id)