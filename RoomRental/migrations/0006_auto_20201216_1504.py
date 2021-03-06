# Generated by Django 3.1.4 on 2020-12-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomRental', '0005_auto_20201216_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='movein_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
