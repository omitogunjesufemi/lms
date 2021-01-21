from django.urls import path
from lms.lms_app.lms_view.enrollment_view import views

urlpatterns = [
    path('initiate/<int:course_id>', views.initiate_enrollment, name='initiate_enrollment'),
    path('list', views.list_enrollments, name='list_enrollment'),
    path('unenroll/<int:enrollment_id>', views.cancel_enrollment, name='unenroll'),
]