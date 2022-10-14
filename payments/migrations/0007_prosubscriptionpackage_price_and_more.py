# Generated by Django 4.0.3 on 2022-04-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_anonymousunlockspackage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='prosubscriptionpackage',
            name='price',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prosubscriptionpackage',
            name='tag',
            field=models.CharField(default='all_access_sub', max_length=36),
        ),
        migrations.AlterField(
            model_name='anonymousunlockspackage',
            name='stripe_price_id',
            field=models.CharField(max_length=96),
        ),
        migrations.AlterField(
            model_name='anonymousunlockspackage',
            name='stripe_product_id',
            field=models.CharField(max_length=96),
        ),
        migrations.AlterField(
            model_name='prosubscriptionpackage',
            name='stripe_price_id',
            field=models.CharField(max_length=96),
        ),
        migrations.AlterField(
            model_name='prosubscriptionpackage',
            name='stripe_product_id',
            field=models.CharField(max_length=96),
        ),
    ]
