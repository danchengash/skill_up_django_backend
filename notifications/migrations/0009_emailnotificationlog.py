# Generated by Django 4.0.3 on 2022-06-04 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0008_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailNotificationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_sent_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='email_notification_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Email Notification Log',
                'verbose_name_plural': 'Email Notification Logs',
                'ordering': ['-id'],
            },
        ),
    ]