from django.urls import path
from lms_app.lms_view.assessment_view import views

urlpatterns = [
    path('create', views.create_assessment, name='create_assessment'),
    path('list', views.list_assessments, name='list_assessment'),
    path('assigned', views.list_assessments_for_students, name='student_assessments'),
    path('uploaded', views.list_assessments_for_tutor, name='tutor_assessments'),
    path('api/tutor', views.tutor_assessments, name='tutor_assessment_api'),
    path('api/student', views.student_assessments, name='student_assessment_api'),
    path('detail/<int:assessment_id>', views.assessment_details, name='assessment_details'),
    path('activate/<int:assessment_id>', views.activate, name='activate'),
    path('deactivate/<int:assessment_id>', views.deactivate, name='deactivate'),
    path('update/<int:assessment_id>', views.update_assessment, name='update_assessment'),
    path('delete/<int:assessment_id>', views.delete_assessment, name='delete_assessment'),
]