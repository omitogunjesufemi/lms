from django.shortcuts import redirect


def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name__exact='staffs').exists():
                return redirect('')
            elif request.user.groups.filter(name__exact='passengers').exists():
                return redirect('')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function
