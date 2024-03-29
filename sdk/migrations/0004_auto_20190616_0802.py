# Generated by Django 2.2.2 on 2019-06-16 02:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdk', '0003_auto_20190615_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 16, 8, 2, 2, 432987), max_length=8),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=128),
        ),
        migrations.AlterField(
            model_name='signup',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 16, 8, 2, 2, 431485)),
        ),
    ]
