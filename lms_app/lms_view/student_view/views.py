import uuid

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

from lms_app.lms_dto.StudentDto import *
from lms_app.service_controllers import service_controller, User, Student


def register_student(request):
    user_list = []
    users = User.objects.all()
    for user in users:
        user_list.append(user.username)

    context = {
        'user_list': user_list,
        'message': 'username already taken'

    }
    student = __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved'] == 'success':
        username = student.username
        password = student.password
        user: User = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name__exact='students').exists():

                return redirect('student_details')
            return redirect('register')
    return render(request, 'student/register.html', context)


@login_required(login_url='login')
def edit_student(request):
    if request.user.has_perm('lms_app.change_student'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)
        try:
            user_id = request.user.id
            student = service_controller.student_management_service().details(user_id)
            student_id = student.id
        except Student.DoesNotExist as e:
            print('You are not registered yet!')
            raise e

        context = {
            'student': student,
            'l_as_list': l_as_list,
            'student_id': student_id,
            'presently': 'User Profile',
        }

        edited_student = __edit_if_post_method(request, student_id, context)
        if edited_student is not None:
            context['student'] = edited_student
            messages.add_message(request, messages.SUCCESS, 'Successfully updated.')
            return redirect('edit_student')
        return render(request, 'student/edit_profile.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def list_student(request):
    if request.user.has_perm('lms_app.view_student'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)
        username = request.user.username
        students = service_controller.student_management_service().list()
        context = {
            'students': students,
            'username': username,
            'l_as_list': l_as_list,
        }
        return render(request, 'student/list_student.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


def todo_list(request):
    if request.user.has_perm('lms_app.view_assessment'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)
        username = request.user.username
        user_id = request.user.id
        student = service_controller.student_management_service().details(user_id)
        student_id = student.id

        context = {
            'username': username,
            'student_id': student_id,
            'presently': 'To-Do List',
            'l_as_list': l_as_list,
        }
        return render(request, 'student/todo_assessments.html', context)
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def list_student_for_courses(request, course_id):
    if request.user.has_perm('lms_app.view_student'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)
        username = request.user.username
        students = service_controller.student_management_service().list_student_for_course(course_id)
        context = {
            'students': students,
            'username': username,
            'l_as_list': l_as_list,
        }
        return render(request, 'student/list_student.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def student_profile(request):
    if request.user.has_perm('lms_app.view_student'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        last_login = request.user.last_login
        user_id = request.user.id
        student = service_controller.student_management_service().details(user_id)
        student_id = student.id

        current_period = datetime.now()
        today_date = current_period.date()

        today_time = current_period.time()


        context = {
            'student': student,
            'username': username,
            'l_as_list': l_as_list,
            'presently': 'Dashboard',
            'last_login': last_login,
            'today_date': today_date,
            'today_time': today_time,
        }
        return render(request, 'student/student_dashboard.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def student_details_for_admin(request, student_id):
    if request.user.has_perm('lms_app.view_student'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        student_ = Student.objects.get(id=student_id)
        student_id = student_.id

        user_id = student_.user.id
        student = service_controller.student_management_service().details(user_id)

        enrollments = service_controller.enrollment_management_service().list_enrollment_for_student(student_id)
        enrollment_len = len(enrollments)

        # Getting all Assessments for Student
        assessments = service_controller.assessment_management_service().list_assessment_for_student(student_id)
        assessment_len = len(assessments)

        # Getting all sittings and attempted assessments by Student
        sittings = service_controller.sitting_management_service().list_of_sitting_for_student_assessment(student_id)
        sitting_len = len(sittings)

        sitting_list = []
        for sitting in sittings:
            for assessment in assessments:
                if sitting.assessment_id == assessment.id:
                    sitting_list.append(sitting.assessment_id)

        context = {
            'student': student,
            'enrollments': enrollments,
            'enrollment_len': enrollment_len,
            'sitting_len': sitting_len,
            'sitting_list': sitting_list,
            'assessments': assessments,
            'assessment_len': assessment_len,
            'username': username,
            'sittings': sittings,
            'l_as_list': l_as_list,
        }
        return render(request, 'student/student_profile.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(redirect_field_name='next')
def delete_student(request, student_id):
    if request.user.has_perm('lms_app.delete_student'):
        try:
            service_controller.student_management_service().delete(student_id)
            return redirect('admin_details')
        except Student.DoesNotExist as e:
            print('This student does not exist!')
            raise e
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)



def __set_student_attribute_request(request: HttpRequest):
    register_student_dto = RegisterStudentDto()
    register_student_dto.first_name = ""
    register_student_dto.username = request.POST['username']
    __get_student_attribute_request(request, register_student_dto)
    return register_student_dto


def __get_student_attribute_request(request: HttpRequest, register_student_dto):
    register_student_dto.first_name = ""
    register_student_dto.last_name = ""
    register_student_dto.phone = ""
    register_student_dto.email = request.POST['email']
    register_student_dto.password = request.POST['password']
    register_student_dto.confirm_password = request.POST['confirm_password']


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            student = __set_student_attribute_request(request)
            password = student.password
            confirm_password = student.confirm_password

            if password == confirm_password:
                student.registration_number = str(uuid.uuid4()).replace('-', '')[0:10].upper()
                service_controller.student_management_service().register(student)
                context['saved'] = 'success'
                return student
            else:
                context['saved'] = 'fail'
        except Exception as e:
            print('This Student was not registered')
            raise e


# Editing Student
def __edit_student_attribute_request(request, student_id):
    edit_student_dto = EditStudentDto()
    edit_student_dto.first_name = request.POST['first_name']
    edit_student_dto.last_name = request.POST['last_name']
    edit_student_dto.phone = request.POST['phone']
    edit_student_dto.email = request.POST['email']
    edit_student_dto.username = request.POST['username']
    edit_student_dto.id = student_id
    return edit_student_dto


def __edit_if_post_method(request, student_id, context):
    if request.method == 'POST':
        try:
            student = __edit_student_attribute_request(request, student_id)
            service_controller.student_management_service().edit(student_id, student)
            context['saved'] = 'success'
            return student
        except Exception as e:
            print('This Student was not registered')
            raise e