# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor', models.CharField(max_length=30)),
                ('acquisition_date', models.DateField()),
                ('signal', models.CharField(max_length=60)),
                ('timestamp', models.DateTimeField()),
                ('value', models.FloatField()),
            ],
        ),
    ]
