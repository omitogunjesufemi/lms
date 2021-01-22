import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, FileResponse, Http404
from django.shortcuts import render, redirect
from lms_app.lms_dto.AppointmentDto import *
from lms_app.models import Appointment, Apply
from lms_app.service_controllers import service_controller


@login_required(login_url='login')
def initiate_appointment(request, course_id, tutor_id, apply_id):
    if request.user.is_superuser:
        context = {

        }
        appoint2 = __initiate_appointment_method(request, course_id, tutor_id, apply_id, context)
        apply = Apply.objects.get(id=apply_id)
        apply.status = True
        apply.save()
        if appoint2 == 1:
            return redirect('admin_details')
        else:
            return render(request, 'enrollment/error_message.html', context)
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(redirect_field_name='next')
def start_appointment(request):
    if request.user.is_superuser:
        username = request.user.username

        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        applications = service_controller.apply_management_service().list()
        courses = service_controller.course_management_service().list()
        tutors = service_controller.tutor_management_service().list()

        context = {
            'username': username,
            'l_as_list': l_as_list,
            'applications': applications,
            'courses': courses,
            'tutors': tutors,
        }
        return render(request, 'appointment/initiate_appointment.html', context)
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)

def update_appointment(request, course_id):
    context = {

    }
    return render(request, '', context)


@login_required(login_url='login')
def list_appointments(request):
    if request.user.is_superuser:
        username = request.user.username
        appointments = service_controller.appointment_management_service().list()
        context = {
            'username': username,
            'appointments': appointments,
        }
        return render(request, 'appointment/list_appointment.html', context)
    else:
        context = {
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)

def appointment_details(request):
    username = request.user.username

    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    user_id = request.user.id
    tutor_id = service_controller.tutor_management_service().details(user_id)

    appointment = service_controller.appointment_management_service().details(tutor_id)
    context = {

    }
    return render(request, '', context)


@login_required(login_url='login')
def delete_appointment(request, appointment_id):
    if request.user.has_perm('lms_app.delete_appointment'):
        try:
            service_controller.appointment_management_service().delete(appointment_id)
        except Appointment.DoesNotExist as e:
            print('This appointment does not exist!')
            return Http404
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)



def __set_appointment_attribute_request(request: HttpRequest):
    initiate_appointment_dto = InitiatedAppointmentDto()
    initiate_appointment_dto.date_appointed = datetime.date.today()
    return initiate_appointment_dto


def __initiate_appointment_method(request, course_id, tutor_id, apply_id, context):
    try:
        appointment = __set_appointment_attribute_request(request)
        appointment.tutors_id = tutor_id
        appointment.course_id = course_id
        tutor_id = appointment.tutors_id
        if Appointment.objects.filter(course_id=course_id, tutors_id=tutor_id).exists():
            context['saved'] = 'failed'
            context['message'] = 'The tutor has already been appointed for the chosen course. Please select another course!'
            return 0
        else:
            service_controller.appointment_management_service().register(appointment)
            context['saved'] = 'success'
            return 1

    except Exception as e:
        print('This Course-Appointment could not be completed')
        raise e