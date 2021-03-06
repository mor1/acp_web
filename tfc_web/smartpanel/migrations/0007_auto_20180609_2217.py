# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-09 21:17
from __future__ import unicode_literals

from uuid import uuid4

from django.db import migrations, models


def add_defaults(apps, schema_editor):
    Layout = apps.get_model('smartpanel', 'Layout')
    Display = apps.get_model('smartpanel', 'Display')
    for layout in Layout.objects.all():
        Layout.objects.filter(pk=layout.pk).update(slug=str(uuid4())[24:])
    for display in Display.objects.all():
        Display.objects.filter(pk=display.pk).update(slug=str(uuid4())[24:])


class Migration(migrations.Migration):

    dependencies = [
        ('smartpanel', '0006_auto_20180609_2159'),
    ]

    operations = [
        migrations.RunPython(add_defaults, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='display',
            name='slug',
            field=models.SlugField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='layout',
            name='slug',
            field=models.SlugField(max_length=12, unique=True),
        ),
    ]
