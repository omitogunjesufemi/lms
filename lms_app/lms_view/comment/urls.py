from django.urls import path
from lms.lms_app.lms_view.comment import views

urlpatterns = [
    path('add/<int:assessment_id>', views.add_comment, name='comment'),
]