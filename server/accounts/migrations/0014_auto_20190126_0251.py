# Generated by Django 2.1.5 on 2019-01-26 02:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20190122_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 28, 2, 51, 36, 860850, tzinfo=utc)),
        ),
    ]