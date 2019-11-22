# Generated by Django 2.2.2 on 2019-06-20 09:29

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sdk', '0026_auto_20190620_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Follow',
            field=models.ManyToManyField(blank=True, related_name='follow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='signup',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 20, 14, 59, 52, 353525)),
        ),
    ]
