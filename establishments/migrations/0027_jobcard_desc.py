# Generated by Django 4.0.3 on 2022-05-24 19:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0026_alter_jobcard_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcard',
            name='desc',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
