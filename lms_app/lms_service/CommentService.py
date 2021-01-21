from abc import ABCMeta, abstractmethod
from typing import List

from lms.lms_app.lms_dto.CommentDto import CommentDto
from lms.lms_app.lms_repository.CommentRepository import CommentRepository


class CommentManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: CommentDto):
        """Create a comment"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, assessment_id, model: CommentDto):
        """Update a comment"""
        raise NotImplementedError

    @abstractmethod
    def list(self, assessment_id) -> List[CommentDto]:
        """List Comments"""
        raise NotImplementedError

    def details(self, comment_id) -> CommentDto:
        """Details of a particular Comment"""
        raise NotImplementedError

    def delete(self, comment_id):
        """Delete a comment"""
        raise NotImplementedError


class DefaultCommentManagementService(CommentManagementService):
    repository = CommentRepository

    def __init__(self, repository: CommentRepository):
        self.repository = repository

    def register(self, model: CommentDto):
        return self.repository.register(model)

    def edit(self, comment_id, model: CommentDto):
        return self.repository.edit(model)

    def list(self, assessment_id) -> List[CommentDto]:
        return self.repository.list(assessment_id)

    def details(self, comment_id) -> CommentDto:
        return self.repository.details(comment_id)

    def delete(self, comment_id):
        return self.repository.delete(comment_id)