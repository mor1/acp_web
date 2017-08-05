# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 17:03
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csn', '0002_sensordata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('info', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=100)),
                ('info', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.RemoveField(
            model_name='lwapplication',
            name='id',
        ),
        migrations.RemoveField(
            model_name='lwdevice',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='device',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='device_type',
        ),
        migrations.AddField(
            model_name='sensordata',
            name='data_format',
            field=models.CharField(choices=[('ascii_hex', 'ascii_hex'), ('ascii', 'ascii'), ('binary', 'binary'), ('other', 'other')], max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='sensor_id',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='sensor_type',
            field=models.CharField(choices=[('LWDevice', 'LoRaWAN Device')], max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='source_type',
            field=models.CharField(choices=[('Everynet', 'Everynet Network')], max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lwdevice',
            name='dev_addr',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^[0-9a-fA-F]+$', 'Needs to be hexadecimal'), django.core.validators.MinLengthValidator(8)]),
        ),
        migrations.AlterField(
            model_name='lwdevice',
            name='dev_eui',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-fA-F]+$', 'Needs to be hexadecimal'), django.core.validators.MinLengthValidator(16)]),
        ),
        migrations.AlterField(
            model_name='lwdevice',
            name='nwkskey',
            field=models.CharField(max_length=32, validators=[django.core.validators.RegexValidator('^[0-9a-fA-F]+$', 'Needs to be hexadecimal'), django.core.validators.MinLengthValidator(32)]),
        ),
        migrations.AlterUniqueTogether(
            name='sensor',
            unique_together=set([('sensor_id', 'type')]),
        ),
        migrations.AddField(
            model_name='lwapplication',
            name='destination_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='csn.Destination'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lwdevice',
            name='sensor_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='csn.Sensor'),
            preserve_default=False,
        ),
    ]