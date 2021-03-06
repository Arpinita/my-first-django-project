# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 06:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0002_auto_20171128_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Animals',
            },
        ),
        migrations.AlterModelOptions(
            name='animals',
            options={},
        ),
        migrations.AlterField(
            model_name='animals',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.Owner'),
        ),
    ]
