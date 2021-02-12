from lms_app.lms_dto.QuestionDto import *
from lms_app.models import Question, Assessment
from typing import List
from abc import ABCMeta, abstractmethod


class QuestionRepository(metaclass=ABCMeta):
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

    @abstractmethod
    def details(self, question_id) -> GetQuestionDto:
        """Details of a question for an assessment"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, question_id):
        """Delete a question for an assessment"""
        raise NotImplementedError


class DjangoORMQuestionRepository(QuestionRepository):
    def register(self, model: SetQuestionDto):
        question = Question()
        question.assessment_id = model.assessment_id
        question.question_title = model.question_title
        question.question_content = model.question_content
        question.answer = model.answer
        question.choice1 = model.choice1
        question.choice2 = model.choice2
        question.choice3 = model.choice3
        question.choice4 = model.choice4
        question.assigned_mark = model.assigned_mark
        question.save()

        assessment = Assessment.objects.get(id=question.assessment_id)
        total_score_for_assessment = int(assessment.total_score) + int(question.assigned_mark)
        assessment.total_score = total_score_for_assessment
        assessment.save()

    def edit(self, question_id, model: UpdateQuestionDto):
        try:
            question = Question.objects.get(id=question_id)
            question.id = question_id
            question.question_title = model.question_title
            question.question_content = model.question_content
            question.answer = model.answer
            question.choice1 = model.choice1
            question.choice2 = model.choice2
            question.choice3 = model.choice3
            question.choice4 = model.choice4

            assessment = question.assessment.id
            total_score_for_assessment = int(assessment.total_score) - int(question.assigned_mark)

            question.assigned_mark = model.assigned_mark
            question.save()

            assessment.total_score = int(total_score_for_assessment) + int(question.assigned_mark)
            assessment.save()
        except Question.DoesNotExist as e:
            print('This question was never set!')
            raise e

    def list(self) -> List[ListQuestionDto]:
        questions = list(Question.objects.values('id',
                                                 'question_title',
                                                 'assigned_mark',
                                                 'assessment_id',
                                                 'assessment__question__question_content',
                                                 'assessment__question__choice1',
                                                 'assessment__question__choice2',
                                                 'assessment__question__choice3',
                                                 'assessment__question__choice4',
                                                 'answer',

                                                 ))
        question_list: List[ListQuestionDto] = []
        for question in questions:
            test = ListQuestionDto()
            test.id = question['id']
            test.question_title = question['question_title']
            test.question_content = question['assessment__question__question_content']
            test.answer = question['answer']
            test.choice1 = question['assessment__question__choice1']
            test.choice2 = question['assessment__question__choice2']
            test.choice3 = question['assessment__question__choice3']
            test.choice4 = question['assessment__question__choice4']
            test.assessment_id = question['assessment_id']
            test.assigned_mark = question['assigned_mark']
            question_list.append(test)
        return question_list

    def list_question_for_tutor(self, tutor_id) -> List[ListQuestionDto]:
        questions = list(Question.objects.values('id',
                                                 'question_title',
                                                 'assigned_mark',
                                                 'assessment_id',
                                                 'question_content',
                                                 'choice1',
                                                 'choice2',
                                                 'choice3',
                                                 'choice4',
                                                 'answer',
                                                 'assessment__course__tutors',

                                                 ))
        question_list: List[ListQuestionDto] = []
        for question in questions:
            if tutor_id == question['assessment__course__tutors']:
                test = ListQuestionDto()
                test.id = question['id']
                test.question_title = question['question_title']
                test.question_content = question['question_content']
                test.answer = question['answer']
                test.choice1 = question['choice1']
                test.choice2 = question['choice2']
                test.choice3 = question['choice3']
                test.choice4 = question['choice4']
                test.assessment_id = question['assessment_id']
                test.assigned_mark = question['assigned_mark']
                question_list.append(test)
        return question_list

    def list_for_assessment(self, assessment_id) -> List[ListQuestionDto]:
        questions = list(Question.objects.values('id',
                                                 'question_title',
                                                 'assigned_mark',
                                                 'assessment_id',
                                                 'question_content',
                                                 'choice1',
                                                 'choice2',
                                                 'choice3',
                                                 'choice4',
                                                 'answer',

                                                 ))
        question_list: List[ListQuestionDto] = []
        for question in questions:
            if assessment_id == question['assessment_id']:
                test = ListQuestionDto()
                test.id = question['id']
                test.question_title = question['question_title']
                test.question_content = question['question_content']
                test.answer = question['answer']
                test.choice1 = question['choice1']
                test.choice2 = question['choice2']
                test.choice3 = question['choice3']
                test.choice4 = question['choice4']
                test.assessment_id = question['assessment_id']
                test.assigned_mark = question['assigned_mark']
                question_list.append(test)
        return question_list

    def details(self, question_id) -> GetQuestionDto:
        try:
            question = Question.objects.get(id=question_id)
            test = GetQuestionDto()
            test.id = question.id
            test.assessment_id = question.assessment.id
            test.question_title = question.question_title
            test.question_content = question.question_content
            test.answer = question.answer
            test.choice1 = question.choice1
            test.choice2 = question.choice2
            test.choice3 = question.choice3
            test.choice4 = question.choice4
            test.assigned_mark = question.assigned_mark
            return test
        except Question.DoesNotExist as e:
            print('This question was never set!')
            raise e

    def delete(self, question_id):
        try:
            Question.objects.get(question_id).delete()
        except Question.DoesNotExist as e:
            print('Cannot delete as the question cannot be found!')
            raise e
