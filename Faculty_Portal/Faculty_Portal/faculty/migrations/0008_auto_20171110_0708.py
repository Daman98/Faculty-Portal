# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0007_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(choices=[(b'0', b'Biosciences and Bioengineering'), (b'2', b'Chemical Engineering'), (b'3', b'Chemistry'), (b'4', b'Civil Engineering'), (b'5', b'Computer Science and Engineering'), (b'6', b'Design'), (b'7', b'Electronics and Electrical Engineering'), (b'8', b'Humanities and Social Sciences'), (b'9', b'Mathematics'), (b'10', b'Mechanical Engineering'), (b'11', b'Physics')], max_length=10),
        ),
    ]
