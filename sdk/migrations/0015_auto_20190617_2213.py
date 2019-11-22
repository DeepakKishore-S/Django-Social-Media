# Generated by Django 2.2.2 on 2019-06-17 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdk', '0014_auto_20190617_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2019, 6, 17, 22, 13, 35, 846715), max_length=8),
        ),
        migrations.AlterField(
            model_name='signup',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 17, 22, 13, 35, 844714)),
        ),
    ]
