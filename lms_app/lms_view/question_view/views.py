from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from lms_app.serializers import *

from lms_app.lms_dto.QuestionDto import *
from lms_app.service_controllers import service_controller, Question, Assessment


@login_required(redirect_field_name='next')
def set_question(request, assessment_id):
    if request.user.has_perm('lms_app.add_question'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        url = request.path_info

        assessment = service_controller.assessment_management_service().details(assessment_id)

        context = {
            'assessment': assessment,
            'username': username,
            'l_as_list': l_as_list,
        }

        __set_question_method(request, context)
        if request.method == 'POST':
            if request.POST.get('submit') == 'Save':
                return redirect('list_question')
            elif request.POST.get('submit') == 'AddMore':
                return redirect(url)
        return render(request, 'question/set_question.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def update_question(request, question_id):
    if request.user.has_perm('lms_app.change_question'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        question = service_controller.question_management_service().details(question_id)

        context = {
            'question': question,
            'username': username,
            'l_as_list': l_as_list,
        }
        if request.method == 'POST':
            __update_question_method(request, question_id, context)
            return redirect('question_details', question_id)
        return render(request, 'question/edit_question.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def list_questions(request):
    if request.user.has_perm('lms_app.view_question'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        questions = service_controller.question_management_service().list()
        context = {
            'questions': questions,
            'username': username,
            'l_as_list': l_as_list,
        }
        return render(request, 'question/list_questions.html', context)
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@api_view(['GET'])
def question_end_point(request, assessment_id):
    if request.method == 'GET':
        questions = service_controller.question_management_service().list_for_assessment(assessment_id=assessment_id)
        serializer = QuestionSerializer(questions, many=True)
        json_data = serializer.data
        return Response(json_data)


@api_view(['GET'])
def tutor_questions(request):
    if request.method == 'GET':
        user_id = request.user.id
        tutor = service_controller.tutor_management_service().details(user_id)
        tutor_id = tutor.id
        questions = service_controller.question_management_service().list_question_for_tutor(tutor_id)
        serializer = TutorQuestionsSerializer(questions, many=True)
        json_data = serializer.data
        return Response(json_data)


@login_required(login_url='login')
def list_questions_for_tutor(request):
    if request.user.has_perm('lms_app.view_question'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username
        user_id = request.user.id
        tutor = service_controller.tutor_management_service().details(user_id)
        tutor_id = tutor.id
        context = {
            'tutor_id': tutor_id,
            'username': username,
            'l_as_list': l_as_list,
        }
        return render(request, 'tutor/tutor_questions.html', context)
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def list_questions_for_assessment(request, assessment_id):
    if request.user.has_perm('lms_app.view_question'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        questions = service_controller.question_management_service().list_for_assessment(assessment_id)

        context = {
            'questions': questions,
            'username': username,
            'l_as_list': l_as_list,
        }
        return render(request, 'question/list_questions.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)

@login_required(login_url='login')
def question_details(request, question_id):
    if request.user.has_perm('lms_app.view_question'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        question = service_controller.question_management_service().details(question_id)

        context = {
            'username': username,
            'question': question,
            'l_as_list': l_as_list,
        }
        return render(request, 'question/get_question.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)

@login_required(login_url='login')
def delete_question(request, question_id):
    if request.user.has_perm('lms_app.delete_question'):
        try:
            question = service_controller.question_management_service().details(question_id)
            qns_score = question.assigned_mark
            assessment = Assessment.objects.get(id=question.assessment_id)
            new_score = assessment.total_score - qns_score
            assessment.total_score = int(new_score)
            service_controller.question_management_service().delete(question_id)
            assessment.save()
            return redirect('tutor_details')
        except Question.DoesNotExist as e:
            print('This question does not exist!')
            raise e
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)

# Setting Question
def __set_question_attribute_request(request: HttpRequest):
    set_question_dto = SetQuestionDto()
    set_question_dto.question_title = request.POST['question_title']
    set_question_dto.assessment_id = request.POST['assessment_id']
    set_question_dto.question_content = request.POST['question_content']
    set_question_dto.answer = request.POST['answer']
    set_question_dto.assigned_mark = request.POST['assigned_mark']
    set_question_dto.choice1 = request.POST['choice1']
    set_question_dto.choice2 = request.POST['choice2']
    set_question_dto.choice3 = request.POST['choice3']
    set_question_dto.choice4 = request.POST['choice4']
    return set_question_dto


def __set_question_method(request, context):
    if request.method == 'POST':
        try:
            question = __set_question_attribute_request(request)
            service_controller.question_management_service().register(question)
            context['saved'] = 'success'
        except Exception as e:
            print('This Question Creation could not be completed')
            raise e


# Updating Question
def __set_update_question_attribute(request: HttpRequest):
    set_question_dto = UpdateQuestionDto()
    set_question_dto.question_title = request.POST['question_title']
    set_question_dto.question_content = request.POST['question_content']
    set_question_dto.answer = request.POST['answer']
    set_question_dto.assigned_mark = request.POST['assigned_mark']
    set_question_dto.choice1 = request.POST['choice1']
    set_question_dto.choice2 = request.POST['choice2']
    set_question_dto.choice3 = request.POST['choice3']
    set_question_dto.choice4 = request.POST['choice4']
    return set_question_dto


def __update_question_method(request, question_id, context):
    if request.method == 'POST':
        try:
            question = __set_update_question_attribute(request)
            service_controller.question_management_service().edit(question_id, question)
            context['saved'] = 'success'
        except Exception as e:
            print('This Question Creation could not be completed')
            raise e
