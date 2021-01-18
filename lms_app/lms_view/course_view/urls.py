from django.urls import path
from lms_app.lms_view.course_view import views

urlpatterns = [
    path('create', views.register_course, name='create_course'),
    path('list', views.list_courses, name='list_courses'),
    path('remove', views.course_delete, name='delete_course'),
]