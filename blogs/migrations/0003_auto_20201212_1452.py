# Generated by Django 3.0.2 on 2020-12-12 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20201212_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 12, 14, 52, 4, 660654)),
        ),
    ]