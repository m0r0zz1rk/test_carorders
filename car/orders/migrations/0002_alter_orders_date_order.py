# Generated by Django 4.1.2 on 2022-10-11 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date_order',
            field=models.DateField(default=datetime.datetime(2022, 10, 11, 16, 47, 9, 637401)),
        ),
    ]