# Generated by Django 3.0.3 on 2021-04-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyre_stock', '0003_auto_20210424_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_stock',
            name='order_number',
            field=models.IntegerField(),
        ),
    ]
