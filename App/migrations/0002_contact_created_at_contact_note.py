# Generated by Django 4.1.1 on 2022-09-24 01:55

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.TextField(default=datetime.datetime(2022, 9, 24, 1, 55, 57, 701303, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]