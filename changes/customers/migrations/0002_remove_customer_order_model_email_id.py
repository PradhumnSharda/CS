# Generated by Django 3.0.3 on 2022-01-11 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_order_model',
            name='email_id',
        ),
    ]
