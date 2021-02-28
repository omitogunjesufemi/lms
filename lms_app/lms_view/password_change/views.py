from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from lms_app.lms_dto.PasswordDto import ChangePasswordDto


@login_required(login_url='login')
def change_password(request):
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)
    username = request.user.username
    context = {
        'username': username,
        'l_as_list': l_as_list,
        'presently': 'Change Password',
    }
    __change_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('login')
    return render(request, 'changepassword.html', context)


def __get_attribute_from_request(request, password_dto):
    password_dto.new_password = request.POST.get('new_password')
    password_dto.confirm_password = request.POST.get('confirm_password')


def __set_attribute_from_request(request):
    password_dto = ChangePasswordDto()
    password_dto.new_password = request.POST.get('new_password')
    __get_attribute_from_request(request, password_dto)
    return password_dto


def __change_if_post_method(request, context):
    if request.method == 'POST':
        try:
            user = __set_attribute_from_request(request)
            password = user.new_password
            confirm_password = user.confirm_password

            user_data = request.user.username
            if password == confirm_password:
                    u = User.objects.get(username=user_data)
                    u.set_password(password)
                    u.save()
                    context['saved'] = 'success'
            else:
                context['saved'] = 'failed'

        except Exception as e:
            context['saved'] = 'error'
            raise e

