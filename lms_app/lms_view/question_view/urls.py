from django.urls import path
from lms.lms_app.lms_view.question_view import views


urlpatterns = [
    path('set/<int:assessment_id>', views.set_question, name='set_question'),
    path('update/<int:question_id>', views.update_question, name='update_question'),
    path('list', views.list_questions, name='list_question'),
    path('delete/<int:question_id>', views.delete_question, name='delete_question'),
    path('details/<int:question_id>', views.question_details, name='question_details'),
    path('get_questions/<int:assessment_id>', views.list_questions_for_assessment, name='list_assessment_question'),
]