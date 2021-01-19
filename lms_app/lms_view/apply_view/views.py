import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect

from lms_app.lms_dto.ApplyDto import ApplyDto
from lms_app.models import Comment, Apply
from lms_app.service_controllers import service_controller, CommentDto


@login_required(redirect_field_name='next')
def apply_for_a_course(request, course_id):

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
    __create_if_post_method(request, course_id, tutor_id, context)
    if request.method == 'POST':
        return redirect('tutor_details')

def edit_application(request, apply_id):
    pass


@login_required(redirect_field_name='next')
def cancel_application(request, apply_id):
    try:
        service_controller.apply_management_service().delete(apply_id)
        return redirect('tutor_details')
    except Apply.DoesNotExist as e:
        print('This application does not exist!')
        raise e


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
            service_controller.apply_management_service().register(application)
            context['saved'] = 'success'
        except Exception as e:
            print('This comment was not registered')
            raise e