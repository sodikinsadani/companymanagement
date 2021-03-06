# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalia', '0012_auto_20170505_1331'),
        ('training', '0002_auto_20170505_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrant',
            fields=[
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='personalia.Employee')),
                ('status_active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
