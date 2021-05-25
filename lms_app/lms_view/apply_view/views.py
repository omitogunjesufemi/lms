from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lms_app.lms_dto.ApplyDto import ApplyDto
from lms_app.models import Apply
from lms_app.serializers import Application
from lms_app.service_controllers import service_controller, Appointment

@login_required(redirect_field_name='next')
def apply_for_a_course(request, course_id):
    if request.user.has_perm('lms_app.add_apply'):

        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username
        user_id = request.user.id
        tutor_id = service_controller.tutor_management_service().details(user_id).id

        context = {
            'username': username,
            'l_as_list': l_as_list,
        }

        appoint = __create_if_post_method(request, course_id, tutor_id, context)
        if appoint == 1:
            __create_if_post_method(request, course_id, tutor_id, context)
            if request.method == 'POST':
                return redirect('tutor_dashboard')
        else:
            return render(request, 'enrollment/error_message.html', context)

    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


def edit_application(request, apply_id):
    pass


@api_view(['GET'])
def list_applications(request):
    if request.method == 'GET':
        applications = service_controller.apply_management_service().list()
        serializer = Application(applications, many=True)
        json_data = serializer.data
        return Response(json_data)


@login_required(redirect_field_name='next')
def cancel_application(request, apply_id):
    if request.user.is_superuser:
        try:
            service_controller.apply_management_service().delete(apply_id)
            return redirect('tutor_dashboard')
        except Apply.DoesNotExist as e:
            print('This application does not exist!')
            raise e
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


def __application_attribute_request(request: HttpRequest, course_id, tutor_id):
    create_application_dto = ApplyDto()
    create_application_dto.tutor_id = tutor_id
    create_application_dto.course_id = course_id
    create_application_dto.qualifications = request.POST['qualifications']
    create_application_dto.file = request.FILES['file_upload']
    return create_application_dto


def __create_if_post_method(request, course_id, tutor_id, context):
    if request.method == 'POST':
        try:
            application = __application_attribute_request(request, course_id, tutor_id)
            if Appointment.objects.filter(course_id=course_id, tutors_id=tutor_id).exists():
                context['saved'] = 'failed'
                context['message'] = 'You are already appointed for the choosen course. Please select another course!'
                return 0
            else:
                service_controller.apply_management_service().register(application)
                context['saved'] = 'success'
                return 1
        except Exception as e:
            print('This application was not registered')
            raise e
