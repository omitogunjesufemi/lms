# Generated by Django 3.1.3 on 2021-01-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0005_auto_20210119_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='file_upload',
            field=models.FileField(upload_to='cv/'),
        ),
    ]
