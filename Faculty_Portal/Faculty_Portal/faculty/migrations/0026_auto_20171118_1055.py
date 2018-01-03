# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0025_profile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='room',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
