# Generated by Django 3.1.3 on 2021-02-02 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0011_auto_20210202_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_slug',
            field=models.TextField(default='', max_length=500),
        ),
    ]