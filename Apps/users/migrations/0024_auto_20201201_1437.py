# Generated by Django 3.1.3 on 2020-12-01 11:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20201201_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='followingList',
            field=models.ManyToManyField(blank=True, null=True, related_name='followerList', to=settings.AUTH_USER_MODEL),
        ),
    ]
