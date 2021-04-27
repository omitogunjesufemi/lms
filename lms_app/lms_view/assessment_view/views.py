import datetime
from typing import List

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lms_app.lms_dto.AssessmentDto import *
from lms_app.lms_dto.CourseDto import *
from lms_app.serializers import *
from lms_app.service_controllers import service_controller, Tutor, Assessment


@login_required(login_url='login')
def create_assessment(request):
    if request.user.has_perm('lms_app.add_assessment'):
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
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def update_assessment(request, assessment_id):
    if request.user.has_perm('lms_app.change_assessment'):
        username = request.user.username
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        assessment = service_controller.assessment_management_service().details(assessment_id)
        context = {
            'l_as_list': l_as_list,
            'username': username,
            'assessment': assessment,

        }
        edited_assessment = __edit_if_post_method(request, assessment_id, context)
        if edited_assessment is not None:
            context['assessment'] = edited_assessment
            return redirect('tutor_details')

        return render(request, 'assessment/edit_assessment.html', context)
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def activate(request, assessment_id):
    assessment = service_controller.assessment_management_service().details(assessment_id)
    assessment.status = 1
    service_controller.assessment_management_service().edit(assessment_id, assessment)
    return redirect('assessment_details', assessment_id)


@login_required(login_url='login')
def deactivate(request, assessment_id):
    assessment = service_controller.assessment_management_service().details(assessment_id)
    assessment.status = 0
    service_controller.assessment_management_service().edit(assessment_id, assessment)
    return redirect('assessment_details', assessment_id)


@login_required(login_url='login')
def list_assessments(request):
    if request.user.has_perm('lms_app.view_assessment'):
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
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def list_assessments_for_students(request):
    if request.user.has_perm('lms_app.view_assessment'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)
        username = request.user.username
        user_id = request.user.id
        student = service_controller.student_management_service().details(user_id)
        student_id = student.id
        assessments = service_controller.assessment_management_service().list_assessment_for_student(student_id)
        assessment_len = len(assessments)

        sittings = service_controller.sitting_management_service().list_of_sitting_for_student_assessment(student_id)

        sitting_list = []
        for sitting in sittings:
            for assessment in assessments:
                if sitting.assessment_id == assessment.id:
                    sitting_list.append(sitting.assessment_id)

        context = {
            'username': username,
            'assessments': assessments,
            'student_id': student_id,
            'presently': 'Assessments',
            'sitting_list': sitting_list,
            'assessment_len': assessment_len,
            'l_as_list': l_as_list,
        }
        return render(request, 'student/student_assessments.html', context)
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(login_url='login')
def list_assessments_for_tutor(request):
    if request.user.has_perm('lms_app.view_assessment'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)
        username = request.user.username
        user_id = request.user.id
        tutor = service_controller.tutor_management_service().details(user_id)
        tutor_id = tutor.id
        assessments = service_controller.assessment_management_service().list_assessment_for_tutor(tutor_id)
        assessment_len = len(assessments)

        context = {
            'username': username,
            'assessments': assessments,
            'tutor_id': tutor_id,
            'presently': 'Assessments',
            'assessment_len': assessment_len,
            'l_as_list': l_as_list,
        }
        return render(request, 'tutor/tutor_assessments.html', context)
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)



@login_required(login_url='login')
def assessment_details(request, assessment_id):
    if request.user.has_perm('lms_app.view_assessment'):
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
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(redirect_field_name='next')
def delete_assessment(request, assessment_id):
    if request.user.has_perm('lms_app.delete_assessment'):
        try:
            service_controller.assessment_management_service().delete(assessment_id)
            return redirect('tutor_details')
        except Assessment.DoesNotExist as e:
            print('This assessment does not exist!')
            raise e
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


# APIs
@api_view(['GET'])
def tutor_assessments(request):
    if request.method == 'GET':
        user_id = request.user.id
        tutor = service_controller.tutor_management_service().details(user_id)
        tutor_id = tutor.id
        assessments = service_controller.assessment_management_service().list_assessment_for_tutor(tutor_id)
        serializer = Assessments(assessments, many=True)
        json_data = serializer.data
        return Response(json_data)


@api_view(['GET'])
def student_assessments(request):
    if request.method == 'GET':
        user_id = request.user.id
        student = service_controller.student_management_service().details(user_id)
        student_id = student.id
        assessments = service_controller.assessment_management_service().list_assessment_for_student(student_id)
        serializer = Assessments(assessments, many=True)
        json_data = serializer.data
        return Response(json_data)


def __set_assessment_attribute_request(request: HttpRequest):
    initiate_assessment_dto = CreateAssessmentDto()
    initiate_assessment_dto.assessment_title = request.POST['assessment_title']
    initiate_assessment_dto.assessment_content = request.POST['assessment_content']
    initiate_assessment_dto.date_due = request.POST['assessment_due_date']
    initiate_assessment_dto.time_due = request.POST['assessment_due_time']
    initiate_assessment_dto.total_score = 0
    initiate_assessment_dto.pass_mark = request.POST['pass_mark']
    initiate_assessment_dto.course_id = request.POST['course_id']
    return initiate_assessment_dto


def __initiate_assessment_method(request, context):
    if request.method == 'POST':
        try:
            assessment = __set_assessment_attribute_request(request)
            service_controller.assessment_management_service().register(assessment)
            context['saved'] = 'success'
        except Exception as e:
            print('This Assessment Creation could not be completed')
            raise e


# Editing
def __edit_assessment_attribute_request(request):
    update_assessment_dto = UpdateAssessmentDto()
    update_assessment_dto.assessment_title = request.POST['assessment_title']
    update_assessment_dto.assessment_content = request.POST['assessment_content']
    update_assessment_dto.date_due = request.POST['assessment_due_date']
    update_assessment_dto.time_due = request.POST['assessment_due_time']
    update_assessment_dto.pass_mark = request.POST['pass_mark']
    update_assessment_dto.total_score = request.POST['total_score']

    try:
        if request.POST['status'] == 'on':
            update_assessment_dto.status = True
        else:
            update_assessment_dto.status = False
    except KeyError:
        update_assessment_dto.status = False

    return update_assessment_dto


def __edit_if_post_method(request, assessment_id, context):
    if request.method == 'POST':
        try:
            assessment = __edit_assessment_attribute_request(request)
            service_controller.assessment_management_service().edit(assessment_id, assessment)
            context['saved'] = 'success'
            return assessment
        except Exception as e:
            print('This assessment was not registered')
            raise e