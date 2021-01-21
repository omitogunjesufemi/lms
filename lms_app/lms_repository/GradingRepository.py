from abc import ABCMeta, abstractmethod
from typing import List

from lms_app.lms_dto.GradingDto import *
from lms_app.models import Grading


class GradingRepository(metaclass=ABCMeta):
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


class DjangoORMGradingRepository(GradingRepository):
    def register(self, model: GradeSittingDto):
        grade = Grading()
        grade.user_grade = model.user_grade
        grade.sitting_id = model.sitting_id
        grade.late_submission = model.late_submission
        grade.failed = model.failed
        grade.save()

    def edit(self, grading_id, model: GradeSittingDto):
        try:
            grade = Grading.objects.get(id=grading_id)
            grade.user_grade = model.user_grade
            grade.save()
        except Grading.DoesNotExist as e:
            print('This sitting cannot be found!')
            raise e

    def list(self) -> List[GradeSittingDto]:
        grades = list(Grading.objects.values('id',
                                             'user_grade',
                                             'sitting_id',
                                             'late_submission',
                                             'failed',
                                                     ))

        grading_list: List[GradeSittingDto] = []
        for grade in grades:
            score = GradeSittingDto()
            score.id = grade['id']
            score.user_grade = grade['user_grade']
            score.sitting_id = grade['sitting_id']
            score.late_submission = grade['late_submission']
            score.failed = grade['failed']
            grading_list.append(score)
        return grading_list

    def details(self, sitting_id) -> GradeSittingDto:
        try:
            grading = Grading.objects.get(sitting_id=sitting_id)
            score = GradeSittingDto()
            score.id = grading.id
            score.user_grade = grading.user_grade
            score.sitting_id = grading.sitting_id
            score.failed = grading.failed
            score.late_submission = grading.late_submission
            return score
        except Grading.DoesNotExist as e:
            print('No Grade found!')
            raise e

    def delete(self, grading_id):
        try:
            Grading.objects.get(grading_id).delete()
        except Grading.DoesNotExist as e:
            print('Cannot delete as you are not enrolled for the course!')
            raise e