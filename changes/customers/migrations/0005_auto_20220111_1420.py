# Generated by Django 3.0.3 on 2022-01-11 14:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20220111_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_order_model',
            name='phone_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
