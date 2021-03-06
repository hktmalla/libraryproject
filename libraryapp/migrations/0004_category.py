# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-28 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_auto_20180224_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.TextField(max_length=30)),
                ('book_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Book')),
            ],
        ),
    ]
