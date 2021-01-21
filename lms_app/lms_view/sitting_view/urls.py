from django.urls import path
from lms.lms_app.lms_view.sitting_view import views


urlpatterns = [
    path('new_sitting/<int:assessment_id>', views.new_sitting, name='new_sitting'),
    path('list', views.list_sittings, name='list_sitting'),
    path('detail/<int:sitting_id>', views.sitting_details, name='sitting_details'),
]