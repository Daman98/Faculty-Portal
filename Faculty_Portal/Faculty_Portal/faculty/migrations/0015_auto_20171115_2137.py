# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0014_auto_20171115_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('0', 'Even Semester'), ('1', 'Odd Semester')], max_length=10),
        ),
    ]
