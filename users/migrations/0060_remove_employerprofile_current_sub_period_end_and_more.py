# Generated by Django 4.0.3 on 2022-04-18 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0059_delete_language_alter_userdocument_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employerprofile',
            name='current_sub_period_end',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='current_sub_period_start',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='stripe_subscription_id',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='subscription_status',
        ),
    ]
