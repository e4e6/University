# Generated by Django 3.1.3 on 2020-12-01 11:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20201201_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 11, 12, 55, 173354, tzinfo=utc), verbose_name='Subscription date'),
        ),
    ]
