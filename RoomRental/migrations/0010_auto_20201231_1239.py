# Generated by Django 3.1.4 on 2020-12-31 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RoomRental', '0009_auto_20201217_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='RoomRental.room'),
        ),
    ]
