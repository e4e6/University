# Generated by Django 3.1.3 on 2020-11-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PuanHesaplamaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siralama', models.IntegerField(default=0)),
                ('hamPuan', models.FloatField(default=0)),
                ('yerlestirmePuan', models.FloatField(default=0)),
            ],
        ),
    ]
