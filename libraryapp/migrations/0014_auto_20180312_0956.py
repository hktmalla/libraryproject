# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-12 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0013_auto_20180312_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='s_id',
            field=models.IntegerField(max_length=20),
        ),
    ]
