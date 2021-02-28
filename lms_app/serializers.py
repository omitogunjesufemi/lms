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

class AssessmentSubmittedForTutor(serializers.ModelSerializer):
    class Meta:
        model = Assessment(models.Model)
        fields = '__all__'