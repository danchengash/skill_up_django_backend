# Generated by Django 4.0.3 on 2022-04-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0012_rename_vacancy_jobapplication_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcard',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]