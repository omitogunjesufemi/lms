from django.urls import path
from lms_app.lms_view.assessment_view import views

urlpatterns = [
    path('create', views.create_assessment, name='create_assessment'),
    path('list', views.list_assessments, name='list_assessment'),
    path('detail/<int:assessment_id>', views.assessment_details, name='assessment_details'),
]