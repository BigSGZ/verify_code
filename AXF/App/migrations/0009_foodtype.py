# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-30 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20180730_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.IntegerField(default=1)),
                ('typename', models.CharField(max_length=16)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]