from django.urls import path
from lms_app.lms_view.appointment_view import views

urlpatterns = [
    path('initiate/<int:course_id>', views.initiate_appointment, name='initiate_appointment'),
    path('list', views.list_appointments, name='list_appointment'),
]