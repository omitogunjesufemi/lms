from django.urls import path
from lms_app.lms_view.tutor_view import views

urlpatterns = [
    path('register', views.register_tutor, name='register_tutor'),
    path('list', views.list_tutors, name='list_tutor'),
    # path('profile', views.tutor_details, name='tutor_details'),
    path('dashboard', views.tutor_profile, name='tutor_dashboard'),
    path('details/<int:tutor_id>', views.tutor_details_for_admin, name='admin_tutor_details'),
    path('edit', views.edit_tutor, name='edit_tutor'),
    path('remove/<int:tutor_id>', views.delete_tutor, name='delete_tutor'),
]