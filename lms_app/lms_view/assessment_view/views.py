import datetime
from typing import List

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from lms_app.lms_dto.AssessmentDto import *
from lms_app.lms_dto.CourseDto import *
from lms_app.service_controllers import service_controller, Tutor


@login_required(login_url='login')
def create_assessment(request):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)
    username = request.user.username
    user_id = request.user.id
    tutor = Tutor.objects.get(user_id=user_id)
    tutors_id = tutor.id
    appointments = service_controller.appointment_management_service().list()
    course_list: List[ListCourseDto] = []
    for appointment in appointments:
        if tutors_id == appointment.tutors_id:
            course = ListCourseDto()
            course.course_id = appointment.course_id
            course.course_title = appointment.course_title
            course_list.append(course)

    context = {
        'username': username,
        'course_list': course_list,
        'l_as_list': l_as_list,
     }
    __initiate_assessment_method(request, context)
    if request.method == 'POST':
        return redirect('list_assessment')
    return render(request, 'assessment/create_assessment.html', context)


@login_required(login_url='login')
def update_assessment(request, course_id):
    username = request.user.username
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)
    context = {
        'l_as_list': l_as_list,
        'username': username,

    }
    return render(request, '', context)


@login_required(login_url='login')
def list_assessments(request):
    # Getting User Group
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)
    username = request.user.username
    assessments = service_controller.assessment_management_service().list()
    context = {
        'username': username,
        'assessments': assessments,
        'l_as_list': l_as_list,
    }
    return render(request, 'assessment/list_assessment.html', context)


@login_required(login_url='login')
def assessment_details(request, assessment_id):
    # Getting User Group
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    username = request.user.username
    assessment = service_controller.assessment_management_service().details(assessment_id)
    context = {
        'username': username,
        'assessment': assessment,
        'l_as_list': l_as_list,
    }
    return render(request, 'assessment/assessment_details.html', context)


def __set_assessment_attribute_request(request: HttpRequest):
    initiate_appointment_dto = CreateAssessmentDto()
    initiate_appointment_dto.assessment_title = request.POST['assessment_title']
    initiate_appointment_dto.assessment_content = request.POST['assessment_content']
    initiate_appointment_dto.date_due = request.POST['assessment_due_date']
    initiate_appointment_dto.time_due = request.POST['assessment_due_time']
    initiate_appointment_dto.total_score = request.POST['total_score']
    initiate_appointment_dto.pass_mark = request.POST['pass_mark']
    initiate_appointment_dto.course_id = request.POST['course_id']
    return initiate_appointment_dto


def __initiate_assessment_method(request, context):
    if request.method == 'POST':
        try:
            assessment = __set_assessment_attribute_request(request)
            service_controller.assessment_management_service().register(assessment)
            context['saved'] = 'success'
        except Exception as e:
            print('This Assessment Creation could not be completed')
            raise e
