# Generated by Django 3.1.5 on 2021-01-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomRental', '0013_auto_20210114_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='movein_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
