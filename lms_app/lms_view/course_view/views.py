from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from lms_app.lms_dto.CourseDto import *
from lms_app.service_controllers import service_controller, User, Course, AdminUser


@login_required(redirect_field_name='next')
def register_course(request):
    if request.user.has_perm('lms_app.add_course'):
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
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def edit_course(request, course_id):
    if request.user.has_perm('lms_app.change_course'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)
        try:
            course = service_controller.course_management_service().details(course_id)
        except Course.DoesNotExist as e:
            print('Course not registered yet!')
            raise e

        context = {
            'course': course,
            'l_as_list': l_as_list,
        }
        edited_course = __edit_if_post_method(request, course_id, context)
        if edited_course is not None:
            context['course'] = edited_course
            return redirect('admin_details')
        return render(request, 'course/edit_course.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


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


def course_details(request, course_id):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    username = request.user.username
    course = service_controller.course_management_service().details(course_id=course_id)
    tutor_list = []
    student_list = []
    students_for_course = service_controller.student_management_service().list_student_for_course(course_id)
    tutor_for_course = service_controller.appointment_management_service().list_tutor_for_course_appointed(course_id)

    if request.user.groups == 'students':
        user_id = request.user.id
        student_id = service_controller.student_management_service().details(user_id).id

        for student in students_for_course:
            if student_id == student.id:
                student_list.append(student_id)

        enrollments = service_controller.enrollment_management_service().list_enrollment_for_student(student_id)
        for enroll in enrollments:
            if course_id == enroll.course_id:
                enrollment = enroll.id
            else:
                enrollment = 0

    elif request.user.groups == 'tutors':
        user_id = request.user.id
        tutor_id = service_controller.tutor_management_service().details(user_id).id

        for tutor in tutor_for_course:
            if tutor_id == tutor.id:
                tutor_list.append(tutor_id)

    if request.user.groups != 'students' or request.user.is_anonymous:
        enrollment = 0

    context = {
        'username': username,
        'l_as_list': l_as_list,
        'course': course,
        'student_list': student_list,
        'tutor_list': tutor_list,
        'enrollment': enrollment,
    }
    return render(request, 'course/course_details.html', context)


def search_course(request):
    search = request.POST.get('search_course').upper()
    courses = service_controller.course_management_service().list()
    search_list = []
    for course in courses:
        course_title = str(course.course_title).upper()
        course_slug = str(course.course_slug).upper()
        if search.upper() in course_title or search in course_slug:
            search_list.append(course)

    context = {
        'courses': search_list,
    }
    return render(request, 'course/list_courses.html', context)


@login_required(redirect_field_name='next')
def course_delete(request, course_id):
    if request.user.has_perm('lms_app.delete_course'):
        try:
            service_controller.course_management_service().delete(course_id)
        except Course.DoesNotExist as e:
            print('This course does not exist!')
            raise e
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


def __set_course_attribute_request(request: HttpRequest):
    create_course_dto = CreateCourseDto()
    create_course_dto.course_title = request.POST['course_title']
    __get_course_attribute_request(request, create_course_dto)
    return create_course_dto


def __get_course_attribute_request(request: HttpRequest, create_course_dto):
    create_course_dto.course_title = request.POST['course_title']
    create_course_dto.course_slug = request.POST['course_slug']


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            course = __set_course_attribute_request(request)
            service_controller.course_management_service().register(course)
            context['saved'] = 'success'
        except Exception as e:
            print('This Course was not registered')
            raise e


# Editing Course
def __edit_course_attribute_request(request, course_id):
    edit_course_dto = EditCourseDto()
    edit_course_dto.course_title = request.POST['course_title']
    edit_course_dto.course_slug = request.POST['course_slug']
    edit_course_dto.file = request.FILES['file_upload']
    edit_course_dto.course_description = request.POST['course_description']
    edit_course_dto.id = course_id
    return edit_course_dto


def __edit_if_post_method(request, course_id, context):
    if request.method == 'POST':
        try:
            course = __edit_course_attribute_request(request, course_id)
            service_controller.course_management_service().edit(course_id, course)
            context['saved'] = 'success'
            return course
        except Exception as e:
            print('This course was not registered')
            raise e
