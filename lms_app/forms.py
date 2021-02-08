from django import forms


class CreateAssessment(forms.Form):
    assessment_title = forms.CharField(max_length=100)
    assessment_content = forms.CharField(widget=forms.Textarea)
    assessment_course = forms.Select()
    assessment_question = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    time_due = forms.TimeField(null=True)
    date_due = forms.DateField(null=True)
