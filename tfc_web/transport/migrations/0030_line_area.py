# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-11 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0029_auto_20171119_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='area',
            field=models.CharField(default='EA', max_length=10),
            preserve_default=False,
        ),
    ]