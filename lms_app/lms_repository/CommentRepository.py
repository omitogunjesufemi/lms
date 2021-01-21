from abc import ABCMeta, abstractmethod
from typing import List

from lms.lms_app.lms_dto.CommentDto import CommentDto
from lms.lms_app.models import Comment


class CommentRepository(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: CommentDto):
        """Create a comment"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, comment_id, model: CommentDto):
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


class DjangoORMCommentRepository(CommentRepository):
    def register(self, model: CommentDto):
        comment = Comment()
        comment.username = model.username
        comment.body = model.body
        comment.assessment_id = model.assessment_id
        comment.date_created = model.date_created
        comment.save()

    def edit(self, comment_id, model: CommentDto):
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.assessment_id = model.assessment_id
            comment.body = model.body
            comment.save()
        except Comment.DoesNotExist as e:
            print('This comment does not exist!')
            raise e

    def list(self, assessment_id) -> List[CommentDto]:
        comments = list(Comment.objects.values('id',
                                               'assessment_id',
                                               'body',
                                               'username',
                                               'date_created',
                                               ))
        comment_list: List[CommentDto] = []
        for comment in comments:
            if assessment_id == comment['assessment_id']:
                task = CommentDto()
                task.id = comment['id']
                task.assessment_id = comment['assessment_id']
                task.body = comment['body']
                task.username = comment['username']
                task.date_created = comment['date_created']
                comment_list.append(task)
        return comment_list

    def details(self, comment_id) -> CommentDto:
        try:
            comment = Comment.objects.get(id=comment_id)
            task = CommentDto()
            task.id = comment.id
            task.assessment_id = comment.assessment_id
            task.body = comment.body
            task.date_created = comment.date_created
            task.username = comment.username
            return task
        except Comment.DoesNotExist as e:
            print('No comment found!')
            raise e

    def delete(self, comment_id):
        try:
            Comment.objects.get(comment_id).delete()
        except Comment.DoesNotExist as e:
            print('Cannot delete as the comment cannot be found!')
            raise e
