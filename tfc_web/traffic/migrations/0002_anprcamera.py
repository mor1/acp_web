# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-07 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ANPRCamera',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('units', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]
