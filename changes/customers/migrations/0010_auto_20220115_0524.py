# Generated by Django 3.0.3 on 2022-01-15 05:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_auto_20220115_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_order_model',
            name='mail_id',
            field=models.CharField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='customer_order_model',
            name='phone_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
