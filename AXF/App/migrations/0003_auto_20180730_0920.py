# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-30 01:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_homenav'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='homenav',
            table='axf_nav',
        ),
    ]