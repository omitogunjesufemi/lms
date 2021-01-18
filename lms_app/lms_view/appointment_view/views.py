import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from lms_app.lms_dto.AppointmentDto import *
from lms_app.models import Appointment
from lms_app.service_controllers import service_controller


@login_required(login_url='login')
def initiate_appointment(request, course_id):
    username = request.user.username
    context = {
        'username': username,

    }
    appoint2 = __initiate_appointment_method(request, course_id, context)
    if appoint2 == 1:
        return redirect('tutor_details')
    else:
        return render(request, 'enrollment/error_message.html', context)


def update_appointment(request, course_id):
    context = {

    }
    return render(request, '', context)


@login_required(login_url='login')
def list_appointments(request):
    username = request.user.username
    appointments = service_controller.appointment_management_service().list()
    context = {
        'username': username,
        'appointments': appointments,
    }
    return render(request, 'appointment/list_appointment.html', context)


def appointment_details(request):
    context = {

    }
    return render(request, '', context)


def __set_appointment_attribute_request(request: HttpRequest):
    initiate_appointment_dto = InitiatedAppointmentDto()
    user_id = request.user.id
    tutors = service_controller.tutor_management_service().details(user_id)
    tutors_id = tutors.id
    initiate_appointment_dto.tutors_id = tutors_id
    initiate_appointment_dto.date_appointed = datetime.date.today()
    return initiate_appointment_dto


def __initiate_appointment_method(request, course_id, context):
    try:
        appointment = __set_appointment_attribute_request(request)
        appointment.course_id = course_id
        tutors_id = appointment.tutors_id
        if Appointment.objects.filter(course_id=course_id, tutors_id=tutors_id).exists():
            context['saved'] = 'failed'
            context['message'] = 'You are already appointed for the chosen course. Please select another course!'
            return 0
        else:
            service_controller.appointment_management_service().register(appointment)
            context['saved'] = 'success'
            return 1

    except Exception as e:
        print('This Course-Appointment could not be completed')
        raise e