# Generated by Django 3.1.3 on 2021-02-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0013_auto_20210203_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='file_upload',
            field=models.FileField(default='', upload_to='courses/<django.db.models.fields.CharField>/display/'),
        ),
    ]