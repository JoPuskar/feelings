# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 16:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0003_auto_20171121_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('uuid', models.CharField(default='', max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FamilyInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('uuid', models.CharField(default='', max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 16, 47, 38, 40080, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='family',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 16, 47, 38, 40080, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='familyinvite',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='groups.Family'),
        ),
        migrations.AddField(
            model_name='familyinvite',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familyinvite_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='familyinvite',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familyinvite_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companyinvite',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='groups.Company'),
        ),
        migrations.AddField(
            model_name='companyinvite',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyinvite_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companyinvite',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyinvite_received', to=settings.AUTH_USER_MODEL),
        ),
    ]
