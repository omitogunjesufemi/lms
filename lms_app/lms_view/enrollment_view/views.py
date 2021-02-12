import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from lms_app.lms_dto.EnrollmentDto import *
from lms_app.models import Enrollment
from lms_app.service_controllers import service_controller


@login_required(login_url='login')
def initiate_enrollment(request, course_id):
    if request.user.has_perm('lms_app.add_enrollment'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        context = {
            'username': username,
            'l_as_list': l_as_list,
        }
        enroll2 = __initiate_enrollment_method(request, course_id, context)
        if enroll2 == 1:
            return redirect('student_details')
        else:
            return render(request, 'enrollment/error_message.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)

@login_required(login_url='login')
def list_enrollments(request):
    if request.user.has_perm('lms_app.view_enrollment'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username
        enrollments = service_controller.enrollment_management_service().list()
        context = {
            'enrollments': enrollments,
            'username': username,
            'l_as_list': l_as_list,
        }
        return render(request, 'enrollment/list_enrollment.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)

@login_required(login_url='login')
def cancel_enrollment(request, enrollment_id):
    if request.user.has_perm('lms_app.delete_enrollment'):
        try:
            service_controller.enrollment_management_service().delete(enrollment_id)
            return redirect('student_details')
        except Enrollment.DoesNotExist as e:
            print('You are not enrolled for this course!')
            raise e
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


def __set_enrollment_attribute_request(request: HttpRequest):
    initiate_enrollment_dto = InitiateEnrollmentDto()
    user_id = request.user.id
    student = service_controller.student_management_service().details(user_id)
    student_id = student.id
    initiate_enrollment_dto.student_id = student_id
    initiate_enrollment_dto.date_enrolled = datetime.date.today()
    return initiate_enrollment_dto


def __initiate_enrollment_method(request, course_id, context):
    try:
        enrollment = __set_enrollment_attribute_request(request)
        enrollment.course_id = course_id
        student_id = enrollment.student_id
        if Enrollment.objects.filter(course_id=course_id, student_id=student_id).exists():
            context['saved'] = 'failed'
            context['message'] = 'You are already enrolled for the choosen course. Please select another course!'
            return 0
        else:
            service_controller.enrollment_management_service().register(enrollment)
            context['saved'] = 'success'
            return 1

    except Exception as e:
        print('This enrollment could not be completed')
        raise e