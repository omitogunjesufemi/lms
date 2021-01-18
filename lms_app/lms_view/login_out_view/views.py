from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_page_post(request):
    resolve_url = request.GET.get('next_url', '/')
    context = {

    }
    username = request.POST.get('username')
    password = request.POST.get('password')
    user: User = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        if user.groups.filter(name__exact='students').exists():
            return redirect(resolve_url)
        elif user.groups.filter(name__exact='tutors').exists():
            return redirect(resolve_url)
    else:
        context['message'] = 'Incorrect Username or Password!'
        return render(request, 'login.html', context)


def login_get(request):
    next_url = request.GET.get('next', '/')
    context = {
        'next_url': next_url,
    }

    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('list_courses')