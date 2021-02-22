from django.urls import path
from lms_app.lms_view.student_view import views

urlpatterns = [
    path('register', views.register_student, name='register_student'),
    path('list', views.list_student, name='list_student'),
    path('list_student/<int:course_id>', views.list_student_for_courses, name='list_student_for_course'),
    path('profile', views.student_details, name='student_details'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('details/<int:student_id>', views.student_details_for_admin, name='admin_student_details'),
    path('edit/<int:student_id>', views.edit_student, name='edit_student'),
    path('remove/<int:student_id>', views.delete_student, name='delete_student'),

]