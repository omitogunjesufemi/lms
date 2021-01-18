"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from lms_app.lms_view.index_view import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registration', views.registration, name='register'),
    path('student/', include('lms_app.lms_view.student_view.urls')),
    path('tutor/', include('lms_app.lms_view.tutor_view.urls')),
    path('course/', include('lms_app.lms_view.course_view.urls')),
    path('enrollment/', include('lms_app.lms_view.enrollment_view.urls')),
    path('appointment/', include('lms_app.lms_view.appointment_view.urls')),
    path('assessment/', include('lms_app.lms_view.assessment_view.urls')),
    path('question/', include('lms_app.lms_view.question_view.urls')),
    path('sitting/', include('lms_app.lms_view.sitting_view.urls')),
    path('grading/', include('lms_app.lms_view.grading_view.urls')),
    path('user/', include('lms_app.lms_view.login_out_view.urls')),
    path('user_edit/', include('lms_app.lms_view.password_change.urls')),
]
