# Generated by Django 4.0.3 on 2022-04-10 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0054_employerprofile_sub_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employerprofile',
            old_name='sub_end_date',
            new_name='current_sub_period_end',
        ),
        migrations.RenameField(
            model_name='employerprofile',
            old_name='sub_start_date',
            new_name='current_sub_period_start',
        ),
    ]
