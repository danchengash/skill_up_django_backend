# Generated by Django 4.0.3 on 2022-04-01 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_jobseekerprofile_hourly_rate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='role',
        ),
    ]
