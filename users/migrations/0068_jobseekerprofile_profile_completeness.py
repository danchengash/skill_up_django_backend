# Generated by Django 4.0.3 on 2022-05-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0067_remove_jobseekerprofile_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseekerprofile',
            name='profile_completeness',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
