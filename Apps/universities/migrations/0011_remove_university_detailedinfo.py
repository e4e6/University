# Generated by Django 3.1.3 on 2020-11-30 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0010_university_detailedinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='detailedInfo',
        ),
    ]
