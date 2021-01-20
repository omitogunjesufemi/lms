import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from lms_app.lms_dto.GradingDto import *
from lms_app.models import Grading
from lms_app.service_controllers import service_controller, Question


@login_required(login_url='login')
def grade_assessment(request, sitting_id):
    if request.user.has_perm('lms_app.add_grading'):
        context = {

        }
        __initiate_grading_method(request, sitting_id=sitting_id, context=context)

        return redirect('student_details')
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)




def __set_grading_attribute_request(request: HttpRequest, sitting_id):
    grade_sitting_dto = GradeSittingDto()
    grade_sitting_dto.sitting_id = sitting_id
    sitting = service_controller.sitting_management_service().details(sitting_id)

    question = sitting.question_list
    questions: list = question.strip('][').split(', ')

    answer = sitting.answer_list
    answers: list = answer.strip('][').split(', ')

    user_answer = sitting.user_answer
    user_answers: list = user_answer.strip('][').split(', ')

    user_score = []

    for qns in questions:
        for ans in answers:
            answers.remove(ans)
            for user_ans in user_answers:
                user_answers.remove(user_ans)
                questions_object = service_controller.question_management_service().details(qns)
                qns_grade = questions_object.assigned_mark
                if ans == user_ans:
                    user_score.append(qns_grade)
                else:
                    user_score.append(0)
                break
            break

    total_score = sum(user_score)

    assessment_id = sitting.assessment_id
    assessment = service_controller.assessment_management_service().details(assessment_id)

    if (sitting.date_submitted > assessment.date_due and sitting.time_submitted > assessment.time_due) or \
            (sitting.date_submitted > assessment.date_due and sitting.time_submitted <= assessment.time_due) or \
            (sitting.date_submitted == assessment.date_due and sitting.time_submitted > assessment.time_due):
        late_submission = 1
    else:
        late_submission = 0

    grade_sitting_dto.late_submission = late_submission

    if total_score >= assessment.pass_mark:
        failed = 0
    else:
        failed = 1

    grade_sitting_dto.failed = failed
    grade_sitting_dto.user_grade = total_score

    return grade_sitting_dto


def __initiate_grading_method(request, sitting_id, context):
    try:
        grade = __set_grading_attribute_request(request, sitting_id)
        service_controller.grading_management_service().register(grade)
        context['saved'] = 'success'

    except Exception as e:
        print('This grading could not be completed')
        raise e