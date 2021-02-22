from abc import ABCMeta, abstractmethod
from typing import List

from lms_app.lms_dto.AssessmentDto import *
from lms_app.models import Assessment


class AssessmentRepository(metaclass=ABCMeta):
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


class DjangoORMAssessmentRepository(AssessmentRepository):
    def register(self, model: CreateAssessmentDto):
        assessment = Assessment()
        assessment.assessment_title = model.assessment_title
        assessment.assessment_content = model.assessment_content
        assessment.course_id = model.course_id
        assessment.total_score = model.total_score
        assessment.pass_mark = model.pass_mark
        assessment.date_due = model.date_due
        assessment.time_due = model.time_due
        assessment.save()

    def edit(self, assessment_id, model: UpdateAssessmentDto):
        try:
            assessment = Assessment.objects.get(id=assessment_id)
            assessment.assessment_title = model.assessment_title
            assessment.assessment_content = model.assessment_content
            assessment.total_score = model.total_score
            assessment.pass_mark = model.pass_mark
            assessment.time_due = model.time_due
            assessment.date_due = model.date_due
            assessment.status = model.status
            assessment.save()
        except Assessment.DoesNotExist as e:
            print('This assessment does not exist!')
            raise e

    def list(self) -> List[ListAssessmentDto]:
        assessments = list(Assessment.objects.values('id',
                                                     'assessment_title',
                                                     'course__course_title',
                                                     'total_score',
                                                     'pass_mark',
                                                     'date_due',
                                                     'time_due',
                                                     'status',
                                                     ))
        assessment_list: List[ListAssessmentDto] = []
        for assessment in assessments:
            task = ListAssessmentDto()
            task.id = assessment['id']
            task.assessment_title = assessment['assessment_title']
            task.course_title = assessment['course__course_title']
            task.total_score = assessment['total_score']
            task.pass_mark = assessment['pass_mark']
            task.date_due = assessment['date_due']
            task.time_due = assessment['time_due']
            task.status = assessment['status']
            assessment_list.append(task)
        return assessment_list

    def list_assessment_for_student(self, student_id) -> List[ListAssessmentDto]:
        assessments = list(Assessment.objects.values('id',
                                                     'assessment_title',
                                                     'course__enrollment__student_id',
                                                     'course__course_title',
                                                     'total_score',
                                                     'pass_mark',
                                                     'date_due',
                                                     'time_due',
                                                     'status',
                                                     ))
        assessment_list: List[ListAssessmentDto] = []
        for assessment in assessments:
            if student_id == assessment['course__enrollment__student_id']:
                task = ListAssessmentDto()
                task.id = assessment['id']
                task.assessment_title = assessment['assessment_title']
                task.course_title = assessment['course__course_title']
                task.total_score = assessment['total_score']
                task.pass_mark = assessment['pass_mark']
                task.date_due = assessment['date_due']
                task.time_due = assessment['time_due']
                task.status = assessment['status']
                assessment_list.append(task)
        return assessment_list

    def list_assessment_for_tutor(self, tutor_id) -> List[ListAssessmentDto]:
        assessments = list(Assessment.objects.values('id',
                                                     'assessment_title',
                                                     'course__appointment__tutors_id',
                                                     'course__course_title',
                                                     'total_score',
                                                     'pass_mark',
                                                     'date_due',
                                                     'time_due',
                                                     'status',
                                                     ))
        assessment_list: List[ListAssessmentDto] = []
        for assessment in assessments:
            if tutor_id == assessment['course__appointment__tutors_id']:
                task = ListAssessmentDto()
                task.id = assessment['id']
                task.assessment_title = assessment['assessment_title']
                task.course_title = assessment['course__course_title']
                task.total_score = assessment['total_score']
                task.pass_mark = assessment['pass_mark']
                task.date_due = assessment['date_due']
                task.time_due = assessment['time_due']
                task.status = assessment['status']
                assessment_list.append(task)
        return assessment_list

    def details(self, assessment_id) -> AssessmentDetailsDto:
        try:
            assessment = Assessment.objects.get(id=assessment_id)
            task = AssessmentDetailsDto()
            task.id = assessment.id
            task.assessment_title = assessment.assessment_title
            task.assessment_content = assessment.assessment_content
            task.course_id = assessment.course.id
            task.course_title = assessment.course.course_title
            task.total_score = assessment.total_score
            task.pass_mark = assessment.pass_mark
            task.date_due = assessment.date_due
            task.time_due = assessment.time_due
            task.status = assessment.status
            return task
        except Assessment.DoesNotExist as e:
            print('No assessment found!')
            raise e

    def delete(self, assessment_id):
        try:
            Assessment.objects.get(id=assessment_id).delete()
        except Assessment.DoesNotExist as e:
            print('Cannot delete as the assessment cannot be found!')
            raise e
