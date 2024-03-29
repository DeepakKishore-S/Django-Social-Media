# Generated by Django 2.2.2 on 2019-06-20 15:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sdk', '0027_auto_20190620_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 20, 20, 47, 40, 936477)),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supporter', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
