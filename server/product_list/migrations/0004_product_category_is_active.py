# Generated by Django 2.1.5 on 2019-01-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_list', '0003_remove_product_category_href'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]