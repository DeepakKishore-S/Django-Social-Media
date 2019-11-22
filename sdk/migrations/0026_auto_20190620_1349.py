# Generated by Django 2.2.2 on 2019-06-20 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdk', '0025_auto_20190620_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='Interested_in',
            field=models.CharField(blank=True, default=' ', max_length=80),
        ),
        migrations.AlterField(
            model_name='signup',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 20, 13, 49, 44, 131937)),
        ),
    ]
