# Generated by Django 4.0.3 on 2022-05-07 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0064_remove_jobseekerprofile_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseekerprofile',
            name='city',
        ),
    ]
