# Generated by Django 3.1.4 on 2021-01-14 06:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RoomRental', '0011_auto_20210113_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='room',
            name='latitude',
            field=models.FloatField(default='126.9780'),
        ),
        migrations.AlterField(
            model_name='room',
            name='longitude',
            field=models.FloatField(default='37.5665'),
        ),
        migrations.AlterField(
            model_name='room',
            name='movein_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.FloatField(default='0'),
        ),
    ]