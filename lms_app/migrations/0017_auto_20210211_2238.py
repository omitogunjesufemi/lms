# Generated by Django 3.1.3 on 2021-02-11 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0016_auto_20210211_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='contents',
            new_name='content',
        ),
    ]
