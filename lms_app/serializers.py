from rest_framework import serializers
from lms_app.models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question(models.Model)
        # fields = ['id', 'assessment',
        #           'question_title',
        #           'content',
        #           'choice1', 'choice2', 'choice3', 'choice4',
        #           'answer',
        #           ]

        fields = '__all__'

class TutorQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question(models.Model)
        fields = '__all__'

class Assessments(serializers.ModelSerializer):
    course_title = serializers.CharField()
    sitting = serializers.IntegerField()
    class Meta:
        model = Assessment(models.Model)
        fields = '__all__'

class Appointments(serializers.Serializer):
    id = serializers.IntegerField()
    course_id = serializers.IntegerField()
    tutors_reg = serializers.CharField()
    course_title = serializers.CharField()
    status = serializers.IntegerField()
    date_appointed = serializers.DateField()


class Enrollments(serializers.ModelSerializer):
    class Meta:
        model = Enrollment(models.Model)
        fields = ['student_id', 'course_id', 'date_enrolled']


class Submissions(serializers.Serializer):
    id = serializers.IntegerField()
    participant_registration_number = serializers.CharField()
    assessment_course = serializers.CharField()
    assessment_title = serializers.CharField()
    assessment_id = serializers.IntegerField()
    date_submitted = serializers.DateField()
    time_submitted = serializers.TimeField()

