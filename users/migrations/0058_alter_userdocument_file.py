# Generated by Django 4.0.3 on 2022-04-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0057_remove_employerprofile_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdocument',
            name='file',
            field=models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name='Document'),
        ),
    ]