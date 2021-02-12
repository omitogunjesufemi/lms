from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AdminUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Tutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    registration_number = models.CharField(max_length=10, default='')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    registration_number = models.CharField(max_length=10, default='')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Course(models.Model):
    course_title = models.CharField(max_length=200)
    course_slug = models.TextField(max_length=500, default='')
    course_prerequisite = models.TextField(max_length=1000, default='')
    course_description = models.TextField(max_length=2048, default='')
    tutors = models.ManyToManyField(Tutor, through='Appointment')
    students = models.ManyToManyField(Student, through='Enrollment')
    file_upload = models.FileField(upload_to=f'courses/display/', default='')

    def __str__(self):
        return f'{self.course_title}'


class Syllabus(models.Model):
    syllabus_header = models.CharField(max_length=500)
    syllabus_body = models.TextField(max_length=2048)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Appointment(models.Model):
    tutors = models.ForeignKey(Tutor, related_name='appointment', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='appointment', on_delete=models.CASCADE)
    date_appointed = models.DateField(null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tutors.registration_number} {self.course.course_title}'


class Enrollment(models.Model):
    student = models.ForeignKey(Student, related_name='enrollment', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollment', on_delete=models.CASCADE)
    date_enrolled = models.DateField(null=True)

    def __str__(self):
        return f'{self.student.registration_number} {self.course.course_title}'


class Assessment(models.Model):
    assessment_title = models.CharField(max_length=200)
    assessment_content = models.TextField(max_length=2048, blank=True)
    course = models.ForeignKey(Course, default='', on_delete=models.CASCADE)
    total_score = models.PositiveBigIntegerField(default=0)
    pass_mark = models.PositiveBigIntegerField(default=0)
    date_due = models.DateField()
    time_due = models.TimeField()
    status = models.BooleanField(default=False)


class Question(models.Model):
    assessment = models.ForeignKey(Assessment, default='', on_delete=models.CASCADE)
    question_title = models.CharField(max_length=200)
    question_content = models.TextField(max_length=2000, blank=True)
    choice1 = models.TextField(max_length=2000, default='')
    choice2 = models.TextField(max_length=2000, default='')
    choice3 = models.TextField(max_length=2000, default='')
    choice4 = models.TextField(max_length=2000, default='')
    answer = models.CharField(max_length=2000, default='choice1')
    assigned_mark = models.IntegerField(default=0)


class Sitting(models.Model):
    participant = models.ForeignKey(Student, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question_list = models.TextField(default='')
    answer_list = models.TextField(default='')
    user_answer = models.TextField(default='')
    date_submitted = models.DateField()
    time_submitted = models.TimeField()


class Grading(models.Model):
    sitting = models.ForeignKey(Sitting, on_delete=models.CASCADE)
    user_grade = models.PositiveBigIntegerField(default=0)
    late_submission = models.PositiveSmallIntegerField(default=0)
    failed = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.user_grade}'


class Comment(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment {self.body} by {self.username}'


class Apply(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    qualifications = models.TextField()
    status = models.BooleanField(default=False)
    file_upload = models.FileField(upload_to='cv/')

    def __str__(self):
        return f'{self.course} {self.status}'

