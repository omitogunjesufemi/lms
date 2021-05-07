from abc import ABCMeta, abstractmethod
from typing import List

from lms_app.lms_dto.SittingDto import *
from lms_app.models import Sitting, Grading


class SittingRepository(metaclass=ABCMeta):
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


class DjangoORMSittingRepository(SittingRepository):
    def register(self, model: NewSittingDto):
        sitting = Sitting()
        sitting.assessment_id = model.assessment_id
        sitting.question_list = model.question_list
        sitting.answer_list = model.answer_list
        sitting.participant_id = model.participant_id
        sitting.user_answer = model.user_answer
        sitting.date_submitted = model.date_submitted
        sitting.time_submitted = model.time_submitted

        sitting.save()
        return sitting

    def edit(self, sitting_id, model: RetakeSittingDto):
        try:
            sitting = Sitting.objects.get(id=sitting_id)
            sitting.assessment.id = model.assessment_id
            sitting.question_list = model.question_list
            sitting.answer_list = model.answer_list
            sitting.participant.id = model.participant_id
            sitting.user_answer = model.user_answer
            sitting.date_submitted = model.date_submitted
            sitting.time_submitted = model.time_submitted

            sitting.save()
            sitting.assessment.save()
        except Sitting.DoesNotExist as e:
            print('You have not taken this test yet!')
            raise e

    def list(self) -> List[ListSittingDto]:
        sittings = list(Sitting.objects.values('id',
                                               'participant__registration_number',
                                               'assessment_id',
                                               'assessment__course',
                                               'assessment__assessment_title',
                                               'date_submitted',
                                               'time_submitted',
                                               'time_submitted',
                                               ))
        sitting_list: List[ListSittingDto] = []
        for sitting in sittings:
            participation = ListSittingDto()
            participation.id = sitting['id']
            participation.participant_registration_number = sitting['participant__registration_number']
            participation.assessment_course = sitting['assessment__course']
            participation.assessment_id = sitting['assessment_id']
            participation.assessment_title = sitting['assessment__assessment_title']
            participation.date_submitted = sitting['date_submitted']
            participation.time_submitted = sitting['time_submitted']
            sitting_list.append(participation)
        return sitting_list

    def list_of_sitting_for_student_assessment(self, student_id) -> List[ListSittingDto]:
        sittings = list(Sitting.objects.values('id',
                                               # 'participant__course__course_title',
                                               'participant_id',
                                               'assessment__course__course_title',
                                               'assessment__assessment_title',
                                               'assessment_id',
                                               'date_submitted',
                                               'time_submitted',
                                               ))
        sitting_list: List[ListSittingDto] = []
        for sitting in sittings:
            if student_id == sitting['participant_id']:
                participation = ListSittingDto()
                participation.id = sitting['id']
                participation.participant_registration_number = sitting['participant_id']
                participation.assessment_course = sitting['assessment__course__course_title']
                participation.assessment_title = sitting['assessment__assessment_title']
                participation.assessment_id = sitting['assessment_id']
                participation.date_submitted = sitting['date_submitted']
                participation.time_submitted = sitting['time_submitted']
                sitting_list.append(participation)
        return sitting_list


    def details(self, sitting_id) -> SittingDetailsDto:
        try:
            sitting = Sitting.objects.get(id=sitting_id)
            participation = SittingDetailsDto()
            participation.id = sitting.id
            participation.participant_id = sitting.participant.id
            participation.participant_registration_number = sitting.participant.registration_number
            participation.participant_first_name = sitting.participant.user.first_name
            participation.participant_last_name = sitting.participant.user.last_name
            participation.assessment_id = sitting.assessment.id
            participation.assessment_title = sitting.assessment.assessment_title
            participation.question_list = sitting.question_list
            participation.answer_list = sitting.answer_list
            participation.user_answer = sitting.user_answer
            participation.time_submitted = sitting.time_submitted
            participation.date_submitted = sitting.date_submitted
            return participation
        except Sitting.DoesNotExist as e:
            print('You have not taken this test yet!')
            raise e

    def delete(self, sitting_id):
        try:
            Grading.objects.get(sitting_id=sitting_id).delete()
            Sitting.objects.get(id=sitting_id).delete()
        except Sitting.DoesNotExist as e:
            print('Cannot delete the sitting!')
            raise e
