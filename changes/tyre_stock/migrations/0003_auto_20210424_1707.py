# Generated by Django 3.0.3 on 2021-04-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyre_stock', '0002_auto_20210220_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_stock',
            name='order_number',
            field=models.IntegerField(max_length=15),
        ),
    ]