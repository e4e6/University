# Generated by Django 3.1.2 on 2020-11-01 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userfollowing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='manager2',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='manager3',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='manager4',
        ),
    ]
