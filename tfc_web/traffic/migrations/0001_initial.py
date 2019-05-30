# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-24 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField()),
                ('entry_lane', models.IntegerField()),
                ('entry_direction', models.IntegerField()),
                ('entry_camera_id', models.CharField(max_length=10)),
                ('entry_absolute_direction', models.CharField(max_length=10)),
                ('plate_encoded', models.CharField(max_length=255)),
                ('plate_country', models.CharField(max_length=10)),
                ('confidence', models.IntegerField()),
                ('exit_time', models.DateTimeField()),
                ('exit_lane', models.IntegerField()),
                ('exit_direction', models.IntegerField()),
                ('exit_camera_id', models.CharField(max_length=10)),
                ('exit_absolute_direction', models.CharField(max_length=10)),
                ('journey_time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='TripChain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_id', models.CharField(max_length=10)),
                ('entry_time', models.DateTimeField()),
                ('vehicle_class', models.CharField(max_length=100)),
                ('total_trip_time', models.DurationField()),
                ('chain_vector', models.CharField(max_length=600)),
                ('chain_vector_time', models.CharField(max_length=600)),
            ],
        ),
    ]