# Generated by Django 4.0.3 on 2022-04-01 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_userdocument_delete_jobseekerdocument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseekerprofile',
            name='identification_card',
        ),
        migrations.RemoveField(
            model_name='jobseekerprofile',
            name='w2_document',
        ),
        migrations.CreateModel(
            name='JobseekerDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobseeker_identity_card', to='users.userdocument')),
                ('jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobseeker_documents', to='users.jobseeker')),
                ('w2_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobseeker_w2_document', to='users.userdocument')),
            ],
        ),
    ]