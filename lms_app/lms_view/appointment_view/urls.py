from django.urls import path
from lms_app.lms_view.appointment_view import views

urlpatterns = [
    path('initiate/<int:course_id>/<int:tutor_id>/<int:apply_id>', views.initiate_appointment, name='initiate_appointment'),
    path('appoint', views.start_appointment, name='appoint'),
    path('list', views.list_appointments, name='list_appointment'),
    path('delete/<int:appointment_id>', views.delete_appointment, name='delete_appointment'),
]