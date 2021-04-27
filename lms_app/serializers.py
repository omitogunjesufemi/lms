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
    class Meta:
        model = Assessment(models.Model)
        fields = '__all__'


class Appointments(serializers.ModelSerializer):
    class Meta:
        model = Appointment(models.Model)
        fields = ['course_id', 'date_appointed', 'status']


class Enrollments(serializers.ModelSerializer):
    class Meta:
        model = Enrollment(models.Model)
        fields = ['student_id', 'course_id', 'date_enrolled']

class Sittings:
    def __init__(self, id, participant_registration_number, assessment_id, assessment_title, date_submitted, time_submitted):
        self.id = id
        self.participant_registration_number = participant_registration_number
        self.assessment_id = assessment_id
        self.assessment_title = assessment_title
        self.date_submitted = date_submitted
        self.time_submitted = time_submitted


class AssessmentSubmittedForTutor(serializers.Serializer):
    id = serializers.IntegerField()
    participant_registration_number = serializers.CharField()
    assessment_title = serializers.CharField()
    assessment_id = serializers.IntegerField()
    date_submitted = serializers.DateField()
    time_submitted = serializers.TimeField()

