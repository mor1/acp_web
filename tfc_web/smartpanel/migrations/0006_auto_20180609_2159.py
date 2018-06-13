# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-09 20:59
from __future__ import unicode_literals

from django.db import migrations, models
from django.db.models import DO_NOTHING


class Migration(migrations.Migration):

    dependencies = [
        ('smartpanel', '0005_auto_20180325_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='layout',
            field=models.ForeignKey(null=True, on_delete=DO_NOTHING,
                                    related_name='displays', to='smartpanel.Layout'),
        ),
        migrations.AddField(
            model_name='display',
            name='slug',
            field=models.SlugField(default='', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='layout',
            name='slug',
            field=models.SlugField(default='', max_length=12),
            preserve_default=False,
        ),
    ]
