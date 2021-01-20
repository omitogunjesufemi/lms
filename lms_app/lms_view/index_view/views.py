from django.shortcuts import render


def index(request):
    username = request.user.username
    l_as_list = []
    for g in request.user.groups.all():
        l_as_list.append(g.name)

    context = {
        'welcome': 'This is the LMS web application for grading student for courses enrolled for!',
        'username': username,
        'l_as_list': l_as_list,

    }
    return render(request, 'index.html', context)


def registration(request):
    context = {

    }
    return render(request, 'registration_page.html', context)
