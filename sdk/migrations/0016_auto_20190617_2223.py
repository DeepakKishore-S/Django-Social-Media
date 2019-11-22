# Generated by Django 2.2.2 on 2019-06-17 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdk', '0015_auto_20190617_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2019, 6, 17, 22, 23, 40, 937746), max_length=8),
        ),
        migrations.AlterField(
            model_name='signup',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 17, 22, 23, 40, 933746)),
        ),
    ]
