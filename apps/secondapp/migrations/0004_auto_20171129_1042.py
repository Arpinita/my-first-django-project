# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0003_auto_20171129_1036'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Owner',
            new_name='Owners',
        ),
    ]
