# Generated by Django 4.2.7 on 2024-11-28 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20191122_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 11, 28, 19, 12, 44, 469977)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2024, 11, 28, 19, 12, 44, 469977)),
        ),
    ]
