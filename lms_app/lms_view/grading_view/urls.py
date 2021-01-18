from django.urls import path
from lms_app.lms_view.grading_view import views

urlpatterns = [
    path('grade/<int:sitting_id>', views.grade_assessment, name='grade_test'),
    path('list', views.list_grading, name='list_grade'),
]
