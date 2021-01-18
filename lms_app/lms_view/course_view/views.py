import uuid
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from lms_app.lms_dto.CourseDto import *
from lms_app.service_controllers import service_controller, User, Course


@login_required(redirect_field_name='next')
def register_course(request):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    username = request.user.username

    context = {
        'username': username,
        'l_as_list': l_as_list,

    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('list_courses')
    return render(request, 'course/register_course.html', context)


def edit_course(request, course_id):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    context = {
        'l_as_list': l_as_list,

    }
    return render(request, '', context)


@login_required(redirect_field_name='next')
def list_courses(request):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    username = request.user.username

    courses = service_controller.course_management_service().list()
    context = {
        'username': username,
        'courses': courses,
        'l_as_list': l_as_list,
    }
    return render(request, 'course/list_courses.html', context)


@login_required(redirect_field_name='next')
def course_details(request):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    username = request.user.username

    context = {
        'username': username,
        'l_as_list': l_as_list,
    }
    return render(request, '', context)


@login_required(redirect_field_name='next')
def course_delete(request, course_id):
    try:
        service_controller.course_management_service().delete(course_id)
    except Course.DoesNotExist as e:
        print('This course does not exist!')
        raise e


def __set_course_attribute_request(request: HttpRequest):
    create_course_dto = CreateCourseDto()
    create_course_dto.course_title = request.POST['course_title']
    __get_course_attribute_request(request, create_course_dto)
    return create_course_dto


def __get_course_attribute_request(request: HttpRequest, create_course_dto):
    create_course_dto.course_title = request.POST['course_title']
    create_course_dto.course_description = request.POST['course_description']


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            course = __set_course_attribute_request(request)
            service_controller.course_management_service().register(course)
            context['saved'] = 'success'
        except Exception as e:
            print('This Course was not registered')
            raise e