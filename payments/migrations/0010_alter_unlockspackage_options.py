# Generated by Django 4.0.3 on 2022-04-12 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_unlockspackage_delete_anonymousunlockspackage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unlockspackage',
            options={'ordering': ['-id'], 'verbose_name': 'Unlocks Package', 'verbose_name_plural': 'Unlocks Packages'},
        ),
    ]
