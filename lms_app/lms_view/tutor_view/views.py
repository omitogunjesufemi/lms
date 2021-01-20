import uuid
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from lms_app.lms_dto.TutorDto import *
from lms_app.service_controllers import service_controller, User, Tutor


def register_tutor(request):

    context = {

    }
    tutor = __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        username = tutor.username
        password = tutor.password
        user: User = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name__exact='tutors').exists():
                return redirect('tutor_details')
            return redirect('')
    return render(request, 'tutor/register_tutor.html', context)


@login_required(login_url='login')
def edit_tutor(request, tutor_id):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    try:
        user_id = request.user.id
        tutor = service_controller.tutor_management_service().details(user_id)
    except Tutor.DoesNotExist as e:
        print('You are not registered yet!')
        raise e

    context = {
        'tutor': tutor,
        'l_as_list': l_as_list,
    }

    edited_tutor = __edit_if_post_method(request, tutor_id, context)
    if edited_tutor is not None:
        context['tutor'] = edited_tutor
        return redirect('tutor_details')
    return render(request, 'tutor/edit_tutor.html', context)


@login_required(login_url='login')
def list_tutors(request):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    tutors = service_controller.tutor_management_service().list()
    context = {
        'tutors': tutors,
        'l_as_list': l_as_list,
    }
    return render(request, 'tutor/list_tutor.html', context)


@login_required(login_url='login')
def tutor_details(request):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)
    user_id = request.user.id
    username = request.user.username
    tutor = service_controller.tutor_management_service().details(user_id)
    tutor_id = tutor.id
    appointments = service_controller.appointment_management_service().list_appoint_for_tutor(tutor_id)
    appointment_len = len(appointments)
    assessments = service_controller.assessment_management_service().list_assessment_for_tutor(tutor_id)
    assessment_len = len(assessments)
    questions = service_controller.question_management_service().list_question_for_tutor(tutor_id)
    question_len = len(questions)

    sittings = service_controller.sitting_management_service().list()
    sitting_list = []

    for sitting in sittings:
        for assessment in assessments:
            if assessment.id == sitting.assessment_id:
                sitting_list.append(sitting)

    sitting_len = len(sitting_list)

    context = {
        'tutor': tutor,
        'appointments': appointments,
        'assessments': assessments,
        'questions': questions,
        'sitting_list': sitting_list,
        'appointment_len': appointment_len,
        'assessment_len': assessment_len,
        'question_len': question_len,
        'sitting_len': sitting_len,
        'username': username,
        'l_as_list': l_as_list,
    }
    return render(request, 'tutor/tutor_profile.html', context)


@login_required(login_url='login')
def tutor_details_for_admin(request, tutor_id):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    username = request.user.username
    tutor_ = Tutor.objects.get(id=tutor_id)
    tutor_id = tutor_.id

    user_id = tutor_.user.id
    tutor = service_controller.tutor_management_service().details(user_id)
    appointments = service_controller.appointment_management_service().list_appoint_for_tutor(tutor_id)
    appointment_len = len(appointments)
    assessments = service_controller.assessment_management_service().list_assessment_for_tutor(tutor_id)
    assessment_len = len(assessments)
    questions = service_controller.question_management_service().list_question_for_tutor(tutor_id)
    question_len = len(questions)

    sittings = service_controller.sitting_management_service().list()
    sitting_list = []

    for sitting in sittings:
        for assessment in assessments:
            if assessment.id == sitting.assessment_id:
                sitting_list.append(sitting)

    sitting_len = len(sitting_list)

    context = {
        'tutor': tutor,
        'appointments': appointments,
        'assessments': assessments,
        'questions': questions,
        'sitting_list': sitting_list,
        'appointment_len': appointment_len,
        'assessment_len': assessment_len,
        'question_len': question_len,
        'sitting_len': sitting_len,
        'username': username,
        'l_as_list': l_as_list,
    }
    return render(request, 'tutor/tutor_profile.html', context)


@login_required(redirect_field_name='next')
def delete_tutor(request, tutor_id):
    try:
        service_controller.tutor_management_service().delete(tutor_id)
        return redirect('admin_details')
    except Tutor.DoesNotExist as e:
        print('This tutor does not exist!')
        raise e


def __set_tutor_attribute_request(request: HttpRequest):
    register_tutor_dto = RegisterTutorDto()
    register_tutor_dto.first_name = request.POST['first_name']
    register_tutor_dto.username = request.POST['username']
    __get_tutor_attribute_request(request, register_tutor_dto)
    return register_tutor_dto


def __get_tutor_attribute_request(request: HttpRequest, register_tutor_dto):
    register_tutor_dto.first_name = request.POST['first_name']
    register_tutor_dto.last_name = request.POST['last_name']
    register_tutor_dto.phone = request.POST['phone']
    register_tutor_dto.email = request.POST['email']
    register_tutor_dto.password = request.POST['password']
    register_tutor_dto.confirm_password = request.POST['confirm_password']


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            tutor = __set_tutor_attribute_request(request)
            password = tutor.password
            confirm_password = tutor.confirm_password
            if password == confirm_password:
                tutor.registration_number = str(uuid.uuid4()).replace('-', '')[0:10].upper()
                service_controller.tutor_management_service().register(tutor)
                context['saved'] = 'success'
                return tutor
            else:
                context['saved'] = 'fail'
        except Exception as e:
            print('This Tutor was not registered')
            raise e


# Editing Student
def __edit_tutor_attribute_request(request, tutor_id):
    edit_tutor_dto = EditTutorDto()
    edit_tutor_dto.first_name = request.POST['first_name']
    edit_tutor_dto.last_name = request.POST['last_name']
    edit_tutor_dto.phone = request.POST['phone']
    edit_tutor_dto.email = request.POST['email']
    edit_tutor_dto.username = request.POST['username']
    edit_tutor_dto.id = tutor_id

    return edit_tutor_dto


def __edit_if_post_method(request, tutor_id, context):
    if request.method == 'POST':
        try:
            tutor = __edit_tutor_attribute_request(request, tutor_id)
            service_controller.tutor_management_service().edit(tutor_id, tutor)
            context['saved'] = 'success'
            return tutor
        except Exception as e:
            print('This tutor was not registered')
            raise e

