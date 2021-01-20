import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from lms_app.models import Comment
from lms_app.service_controllers import service_controller, CommentDto


@login_required(redirect_field_name='next')
def add_comment(request, assessment_id):
    if request.user.has_perm('lms_app.add_comment'):
        l_as_list = []
        for g in request.user.groups.all():
            l_as_list.append(g.name)

        username = request.user.username

        context = {
            'username': username,
            'l_as_list': l_as_list,

        }
        __create_if_post_method(request, assessment_id, context)
        if request.method == 'POST' and context['saved']:
            return redirect('tutor_details')
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


@login_required(redirect_field_name='next')
def comment_details(request, comment_id):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    username = request.user.username

    comment = service_controller.comment_management_service().details(comment_id)

    context = {
        'username': username,
        'l_as_list': l_as_list,
        'comment': comment,

    }
    return render(request, '', context)


@login_required(redirect_field_name='next')
def comment_delete(request, comment_id):
    if request.user.has_perm('lms_app.delete_comment'):
        try:
            service_controller.comment_management_service().delete(comment_id)
        except Comment.DoesNotExist as e:
            print('This course does not exist!')
            raise e
    else:
        context={
            'message': 'You are not authorised'
        }
        return render(request, 'error_message.html', context)


def __set_comment_attribute_request(request: HttpRequest, assessment_id):
    add_comment_dto = CommentDto()
    add_comment_dto.assessment_id = assessment_id
    username = request.user.username
    add_comment_dto.body = request.POST['comment_body']
    add_comment_dto.username = username
    add_comment_dto.date_created = datetime.date.today()
    return add_comment_dto


def __create_if_post_method(request, assessment_id, context):
    if request.method == 'POST':
        try:
            comment = __set_comment_attribute_request(request, assessment_id)
            service_controller.comment_management_service().register(comment)
            context['saved'] = 'success'
        except Exception as e:
            print('This comment was not registered')
            raise e