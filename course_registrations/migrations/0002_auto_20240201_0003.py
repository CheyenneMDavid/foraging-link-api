# Generated by Django 3.2.4 on 2024-02-01 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_registrations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseregistration',
            old_name='course',
            new_name='course_title',
        ),
        migrations.RenameField(
            model_name='courseregistration',
            old_name='name',
            new_name='user_name',
        ),
    ]