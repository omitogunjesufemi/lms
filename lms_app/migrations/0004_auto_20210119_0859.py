# Generated by Django 3.1.3 on 2021-01-19 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifications', models.TextField()),
                ('file_upload', models.FileField(upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms_app.course')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms_app.tutor')),
            ],
        ),
    ]