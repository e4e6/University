# Generated by Django 3.1.3 on 2020-11-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0009_university_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='detailedInfo',
            field=models.CharField(default='', max_length=800),
        ),
    ]
