import uuid
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from lms_app.lms_dto.AdminDto import *
from lms_app.service_controllers import service_controller, User, AdminUser


def register_admin(request):
    context = {

    }
    admin = __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved'] == 'success':
        username = admin.username
        password = admin.password
        user: User = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name__exact='admins').exists():
                return redirect('admin_details')
            return redirect('/')
    return render(request, 'admin/register_admin.html', context)


@login_required(login_url='login')
def edit_admin(request, admin_id):
    if request.user.is_superuser:
        username = request.user.username
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        try:
            user_id = request.user.id
            admin = service_controller.admin_management_service().details(user_id)
        except AdminUser.DoesNotExist as e:
            print('You are not registered yet!')
            raise e

        context = {
            'admin': admin,
            'username': username,
            'l_as_list': l_as_list,
        }

        edited_admin = __edit_if_post_method(request, admin_id, context)
        if edited_admin is not None:
            context['admin'] = edited_admin
            return redirect('admin_details')
        return render(request, 'admin/edit_admin.html', context)
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def list_admins(request):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    admins = service_controller.admin_management_service().list()
    context = {
        'admins': admins,
        'l_as_list': l_as_list,
    }
    return render(request, '', context)


@login_required(login_url='login')
def admin_dashboard(request):
    if request.user.is_superuser:
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)
        user_id = request.user.id
        username = request.user.username
        admin = service_controller.admin_management_service().details(user_id)

        context = {
            'admin': admin,
            'username': username,
            'l_as_list': l_as_list,
        }
        return render(request, 'admin/admin_dashboard.html', context)
    else:
        context = {
            'message': 'You are not authorised!'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def admin_details(request):
    if request.user.is_superuser:
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)
        user_id = request.user.id
        username = request.user.username

        admin = service_controller.admin_management_service().details(user_id)

        tutors = service_controller.tutor_management_service().list()
        tutor_len = len(tutors)

        students = service_controller.student_management_service().list()
        student_len = len(students)

        courses = service_controller.course_management_service().list()
        course_len = len(courses)

        applications = service_controller.apply_management_service().list()
        application_len = len(applications)

        appointments = service_controller.appointment_management_service().list()
        appointment_len = len(appointments)

        assessments = service_controller.assessment_management_service().list()
        assessment_len = len(assessments)

        enrollments = service_controller.enrollment_management_service().list()
        enrollment_len = len(enrollments)

        questions = service_controller.question_management_service().list()
        question_len = len(questions)

        sittings = service_controller.sitting_management_service().list()
        sitting_len = len(sittings)

        context = {
            'admin': admin,
            'tutors': tutors,
            'students': students,
            'courses': courses,
            'applications': applications,
            'appointments': appointments,
            'assessments': assessments,
            'enrollments': enrollments,
            'questions': questions,
            'sittings': sittings,

            'tutor_len': tutor_len,
            'student_len': student_len,
            'course_len': course_len,
            'appointment_len': appointment_len,
            'application_len': application_len,
            'assessment_len': assessment_len,
            'enrollment_len': enrollment_len,
            'question_len': question_len,
            'sitting_len': sitting_len,

            'username': username,
            'l_as_list': l_as_list,
        }
        return render(request, 'admin/admin_profile.html', context)
    else:
        context = {
            'message': 'You are not authorised!'
        }
        return render(request, 'error_message.html', context)


def __set_admin_attribute_request(request: HttpRequest):
    register_admin_dto = RegisterAdminDto()
    register_admin_dto.first_name = request.POST['first_name']
    register_admin_dto.username = request.POST['username']
    __get_admin_attribute_request(request, register_admin_dto)
    return register_admin_dto


def __get_admin_attribute_request(request: HttpRequest, register_admin_dto):
    register_admin_dto.first_name = request.POST['first_name']
    register_admin_dto.last_name = request.POST['last_name']
    register_admin_dto.phone = request.POST['phone']
    register_admin_dto.email = request.POST['email']
    register_admin_dto.password = request.POST['password']
    register_admin_dto.confirm_password = request.POST['confirm_password']


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            admin = __set_admin_attribute_request(request)
            password = admin.password
            confirm_password = admin.confirm_password
            if password == confirm_password:
                service_controller.admin_management_service().register(admin)
                context['saved'] = 'success'
                return admin
            else:
                context['saved'] = 'fail'
        except Exception as e:
            print('This Admin was not registered')
            raise e


# Editing Admin
def __edit_admin_attribute_request(request, admin_id):
    edit_admin_dto = EditAdminDto()
    edit_admin_dto.first_name = request.POST['first_name']
    edit_admin_dto.last_name = request.POST['last_name']
    edit_admin_dto.phone = request.POST['phone']
    edit_admin_dto.email = request.POST['email']
    edit_admin_dto.username = request.POST['username']
    edit_admin_dto.id = admin_id

    return edit_admin_dto


def __edit_if_post_method(request, admin_id, context):
    if request.method == 'POST':
        try:
            admin = __edit_admin_attribute_request(request, admin_id)
            service_controller.admin_management_service().edit(admin_id, admin)
            context['saved'] = 'success'
            return admin
        except Exception as e:
            print('This admin was not registered')
            raise e

