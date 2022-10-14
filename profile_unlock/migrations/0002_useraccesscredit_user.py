# Generated by Django 4.0.3 on 2022-05-29 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_unlock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccesscredit',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='access_credits', to=settings.AUTH_USER_MODEL),
        ),
    ]