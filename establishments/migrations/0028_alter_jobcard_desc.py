# Generated by Django 4.0.3 on 2022-05-24 19:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0027_jobcard_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcard',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]