# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-04 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0010_auto_20180301_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category_title',
            field=models.CharField(choices=[('IT', 'IT'), ('Computer', 'Computer'), ('Electronics', 'Electronics'), ('Civil', 'Civil'), ('Bba', 'BBA')], default=1, max_length=30),
        ),
    ]