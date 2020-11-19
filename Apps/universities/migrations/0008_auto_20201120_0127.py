# Generated by Django 3.1.3 on 2020-11-19 22:27

import Apps.universities.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0007_university_profile_photo_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='cover_photo_path',
        ),
        migrations.RemoveField(
            model_name='university',
            name='images',
        ),
        migrations.RemoveField(
            model_name='university',
            name='profile_photo_file',
        ),
        migrations.RemoveField(
            model_name='university',
            name='profile_photo_path',
        ),
        migrations.AddField(
            model_name='university',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=Apps.universities.models.University.upload_to_func),
        ),
        migrations.AddField(
            model_name='university',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=Apps.universities.models.University.upload_to_func),
        ),
    ]
