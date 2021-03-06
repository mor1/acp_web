# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-17 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authmultitoken', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=256, verbose_name='Value')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referers', to='authmultitoken.Token', verbose_name='Token')),
            ],
        ),
    ]
