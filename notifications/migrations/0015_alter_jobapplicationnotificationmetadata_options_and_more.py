# Generated by Django 4.0.3 on 2022-06-05 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0014_jobapplicationnotificationmetadata_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobapplicationnotificationmetadata',
            options={'ordering': ['-id'], 'verbose_name': 'Job Application Notification Metadata', 'verbose_name_plural': 'Job Application Notification Metadata'},
        ),
        migrations.RemoveField(
            model_name='notification',
            name='job_application_metadata',
        ),
        migrations.AddField(
            model_name='jobapplicationnotificationmetadata',
            name='notification',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='jobcard_notification_metadata', to='notifications.notification'),
            preserve_default=False,
        ),
    ]
