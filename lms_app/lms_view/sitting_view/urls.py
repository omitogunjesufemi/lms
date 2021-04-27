from django.urls import path
from lms_app.lms_view.sitting_view import views


urlpatterns = [
    path('new_sitting/<int:assessment_id>', views.new_sitting, name='new_sitting'),
    path('list', views.list_sittings, name='list_sitting'),
    path('submitted_to_tutor', views.list_submissions_for_tutors, name='submission_for_tutor'),
    path('late_submission', views.list_of_late_submissions_for_tutors, name='late_submissions'),
    path('submissions_to_tutor', views.submissions_for_tutors, name='submissions_for_tutor'),
    path('detail/<int:sitting_id>', views.sitting_details, name='sitting_details'),
    path('delete/<int:sitting_id>', views.delete_sitting, name='delete_sitting'),
]