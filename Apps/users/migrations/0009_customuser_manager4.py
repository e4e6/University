# Generated by Django 3.1.2 on 2020-11-01 18:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201101_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='manager4',
            field=models.ManyToManyField(null=True, related_name='_customuser_manager4_+', to=settings.AUTH_USER_MODEL),
        ),
    ]