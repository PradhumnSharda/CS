# Generated by Django 3.0.3 on 2022-01-11 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyre_stock', '0004_auto_20210424_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tyre_stockmodel',
            name='tyre_name',
            field=models.CharField(error_messages={'unique': 'This Tyre model already exists. Please use another name.'}, max_length=50, unique=True),
        ),
    ]