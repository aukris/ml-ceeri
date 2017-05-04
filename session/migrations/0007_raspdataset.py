# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0006_auto_20170501_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaspDataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('humidity', models.FloatField()),
                ('data3', models.FloatField()),
                ('data4', models.FloatField()),
                ('data5', models.FloatField()),
                ('data6', models.FloatField()),
                ('data7', models.FloatField()),
                ('data8', models.FloatField()),
                ('indexed_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]