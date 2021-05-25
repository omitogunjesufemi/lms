from django.urls import path
from lms_app.lms_view.apply_view import views

urlpatterns = [
    path('apply/<int:course_id>', views.apply_for_a_course, name='tutor_application'),
    path('delete/<int:apply_id>', views.cancel_application, name='cancel_application'),
    path('list', views.list_applications, name='list_applications'),
]