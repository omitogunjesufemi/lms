from django.urls import path
from lms_app.lms_view.admin_view import views

urlpatterns = [
    path('register', views.register_admin, name='register_admin'),
    path('list', views.list_admins, name='list_admins'),
    path('profile', views.admin_details, name='admin_details'),
    path('dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('edit', views.edit_admin, name='edit_admin'),
]
