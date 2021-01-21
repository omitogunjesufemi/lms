from django.urls import path
from lms_app.lms_view.password_change import views

urlpatterns = [
    path('change_password/', views.change_password, name='change_password'),
]