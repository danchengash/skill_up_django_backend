# Generated by Django 4.0.3 on 2022-06-06 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0030_alter_jobcard_is_published'),
        ('notifications', '0019_remove_jobapplicationnotificationmetadata_job_card_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='job_application',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='establishments.jobapplication'),
        ),
        migrations.DeleteModel(
            name='JobApplicationNotificationMetadata',
        ),
    ]
