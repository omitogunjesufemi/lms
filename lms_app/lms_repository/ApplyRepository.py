from abc import ABCMeta, abstractmethod
from typing import List

from lms_app.lms_dto.ApplyDto import ApplyDto
from lms_app.models import Comment, Apply


class ApplyRepository(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: ApplyDto):
        """Create a comment"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, apply_id, model: ApplyDto):
        """Update a comment"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ApplyDto]:
        """List Comments"""
        raise NotImplementedError


    def details(self, apply_id) -> ApplyDto:
        """Details of a particular Comment"""
        raise NotImplementedError

    def delete(self, apply_id):
        """Delete a comment"""
        raise NotImplementedError


class DjangoORMApplyRepository(ApplyRepository):
    def register(self, model: ApplyDto):
        apply = Apply()
        apply.tutor_id = model.tutor_id
        apply.course_id = model.course_id
        apply.qualifications = model.qualifications
        apply.file_upload = model.file
        apply.status = False
        apply.save()

    def edit(self, apply_id, model: ApplyDto):
        try:
            apply = Apply.objects.get(id=apply_id)
            apply.course_id = model.course_id
            apply.qualifications = model.qualifications
            apply.file_upload = model.file
            apply.save()
        except Apply.DoesNotExist as e:
            print('This application does not exist!')
            raise e

    def list(self) -> List[ApplyDto]:
        applications = list(Apply.objects.values('id',
                                                 'tutor_id',
                                                 'course_id',
                                                 'qualifications',
                                                 'status',
                                                 'file_upload'
                                               ))
        application_list: List[ApplyDto()] = []
        for application in applications:
            apply = ApplyDto()
            apply.id = application['id']
            apply.tutor_id = application['tutor_id']
            apply.course_id = application['course_id']
            apply.qualifications = application['qualifications']
            apply.file = application['file_upload']
            apply.status = application['status']
            application_list.append(apply)
        return application_list

    def details(self, apply_id) -> ApplyDto:
        try:
            apply = Apply.objects.get(id=apply_id)
            task = ApplyDto()
            task.id = apply.id
            task.tutor_id = apply.tutor_id
            task.course_id = apply.course_id
            task.qualifications = apply.qualifications
            task.file = apply.file_upload
            task.status = apply.status
            return task
        except Apply.DoesNotExist as e:
            print('No application found!')
            raise e

    def delete(self, apply_id):
        try:
            Apply.objects.get(apply_id).delete()
        except Apply.DoesNotExist as e:
            print('Cannot delete as the application cannot be found!')
            raise e
