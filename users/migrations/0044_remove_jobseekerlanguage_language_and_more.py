# Generated by Django 4.0.3 on 2022-04-04 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_alter_workexperience_end_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseekerlanguage',
            name='language',
        ),
        migrations.AddField(
            model_name='jobseekerlanguage',
            name='name',
            field=models.CharField(default=1, max_length=64, verbose_name='Language'),
            preserve_default=False,
        ),
    ]
