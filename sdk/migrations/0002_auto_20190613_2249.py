# Generated by Django 2.2 on 2019-06-13 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 13, 22, 49, 20, 71099)),
        ),
    ]
