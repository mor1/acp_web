# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-09 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0002_anprcamera'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tripchain',
            index=models.Index(fields=['camera_id', 'entry_time', 'total_trip_time', 'chain_vector'],
                               name='traffic_tri_camera__b956ab_idx'),
        ),
        migrations.AddIndex(
            model_name='tripchain',
            index=models.Index(fields=['camera_id'], name='traffic_tri_camera__837117_idx'),
        ),
        migrations.AddIndex(
            model_name='tripchain',
            index=models.Index(fields=['entry_time'], name='traffic_tri_entry_t_852c39_idx'),
        ),
        migrations.AddIndex(
            model_name='tripchain',
            index=models.Index(fields=['chain_vector'], name='traffic_tri_chain_v_ea459a_idx'),
        ),
        migrations.AddIndex(
            model_name='tripchain',
            index=models.Index(fields=['chain_vector_time'], name='traffic_tri_chain_v_81c57e_idx'),
        ),
    ]