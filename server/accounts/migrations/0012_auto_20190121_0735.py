# Generated by Django 2.1.1 on 2019-01-21 04:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190121_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 4, 35, 2, 33350, tzinfo=utc)),
        ),
    ]
