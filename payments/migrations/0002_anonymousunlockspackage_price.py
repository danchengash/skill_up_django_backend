# Generated by Django 4.0.3 on 2022-04-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymousunlockspackage',
            name='price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]