import datetime
from typing import List

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpRequest
from django.shortcuts import render, redirect
from lms_app.lms_dto.SittingDto import *
from lms_app.service_controllers import service_controller
from django.core.paginator import Paginator
from django.contrib import messages



def welcome(request):
    pass


def success_submit(request):
    pass


@login_required(login_url='login')
def new_sitting(request, assessment_id):
    if request.user.has_perm('lms_app.add_sitting'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        user_id = request.user.id
        student_id = service_controller.student_management_service().details(user_id=user_id).id
        assessment = service_controller.assessment_management_service().details(assessment_id)
        questions = service_controller.question_management_service().list_for_assessment(assessment_id)
        sitting_question_list = []
        sitting_answer_list = []

        i = 1
        list_qns = []

        for question in questions:
            if assessment_id == question.assessment_id:
                sitting_question_list.append(question.id)
                list_qns.append(i)
                sitting_answer_list.append(question.answer)
                i = i+1

        question_count = len(questions)
        paginator = Paginator(questions, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'username': username,
            'assessment': assessment,
            'assessment_id': assessment_id,
            'question': questions,
            'sitting_question_list': sitting_question_list,
            'l_as_list': l_as_list,
            'question_count': question_count,
            'list_qns': list_qns,
            'questions': page_obj,
            'qns_page': page_number,
        }

        sitting = __new_sitting_method(request, sitting_answer_list,
                                        sitting_question_list, student_id, assessment_id, context)
        if request.method == 'POST':
            sitting_id = sitting.id
            return redirect('grade_test', sitting_id)
        return render(request, 'api_question.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def list_sittings(request):
    if request.user.has_perm('lms_app.view_sitting'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        sittings = service_controller.sitting_management_service().list()
        context = {
            'username': username,
            'sittings': sittings,
            'l_as_list': l_as_list,
        }
        return render(request, 'sitting/list_sitting.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def sitting_details(request, sitting_id):
    if request.user.has_perm('lms_app.view_sitting'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        sitting = service_controller.sitting_management_service().details(sitting_id)
        user_grade = service_controller.grading_management_service().details(sitting_id)
        assessment_id = sitting.assessment_id
        assessment = service_controller.assessment_management_service().details(assessment_id)
        questions = service_controller.question_management_service().list_for_assessment(assessment_id)

        question = sitting.question_list
        question_list: list = question.strip('][').split(', ')

        answer = sitting.answer_list
        answers: list = answer.strip('][').split(', ')

        user_answer = sitting.user_answer
        user_answers: list = user_answer.strip('][').split(', ')

        user_choice = dict(zip(question_list, user_answers))
        set_choice = dict(zip(question_list, answers))

        comments = service_controller.comment_management_service().list(assessment_id)
        comment_len = len(comments)

        i = 1
        list_qns = []
        for question in questions:
            if assessment_id == question.assessment_id:
                list_qns.append(i)
                i = i+1

        paginator = Paginator(questions, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'username': username,
            'sitting': sitting,
            'user_grade': user_grade,
            'assessment': assessment,
            'question': questions,
            'questions': page_obj,
            'user_choice': user_choice,
            'set_choice': set_choice,
            'l_as_list': l_as_list,
            'list_qns': list_qns,
            'comments': comments,
            'comment_len': comment_len,
        }
        return render(request, 'sitting/sitting_details.html', context)
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


def delete_sitting(request, sitting_id):
    if request.user.is_superuser:
        service_controller.sitting_management_service().delete(sitting_id)
        return redirect('admin_details')
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


def __set_sitting_attribute_request(request: HttpRequest, sitting_answer_list,
                                    sitting_question_list, student_id, assessment_id):

    new_sitting_dto = NewSittingDto()
    new_sitting_dto.participant_id = student_id
    new_sitting_dto.assessment_id = assessment_id
    new_sitting_dto.answer_list = sitting_answer_list
    new_sitting_dto.question_list = sitting_question_list
    new_sitting_dto.date_submitted = datetime.date.today()
    new_sitting_dto.time_submitted = datetime.datetime.now().time()
    return new_sitting_dto


def __get_answers_from_cookies(request):
    answer_list = []
    user_choice = request.POST.get("answer")
    answers: list = user_choice.split(",")
    for choices in answers:
        answer_list.append(choices)

    return answer_list


def __new_sitting_method(request, sitting_answer_list, sitting_question_list, student_id, assessment_id, context):
    if request.method == 'POST':
        try:
            sitting = __set_sitting_attribute_request(request, sitting_answer_list=sitting_answer_list,
                                                      sitting_question_list=sitting_question_list,
                                                      student_id=student_id, assessment_id=assessment_id)

            sitting.user_answer = __get_answers_from_cookies(request)
            solved_assessment = service_controller.sitting_management_service().register(sitting)
            context['saved'] = 'success'
            return solved_assessment
        except Exception as e:
            print('This Sitting Creation could not be completed')
            raise e
