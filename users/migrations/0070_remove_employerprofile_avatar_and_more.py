# Generated by Django 4.0.3 on 2022-05-16 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0069_remove_user_u_type_user_logged_in_as'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employerprofile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='contact_is_verified',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='phone_number',
        ),
    ]