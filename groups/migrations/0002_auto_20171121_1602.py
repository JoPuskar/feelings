# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 16:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 21, 16, 2, 33, 619377, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='family',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 21, 16, 2, 33, 619377, tzinfo=utc)),
        ),
    ]
