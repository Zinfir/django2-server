# Generated by Django 2.1.5 on 2019-01-27 13:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20190127_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 29, 13, 58, 49, 540904, tzinfo=utc)),
        ),
    ]