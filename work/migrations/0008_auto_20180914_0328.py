# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-13 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0007_auto_20180908_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusamb',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
