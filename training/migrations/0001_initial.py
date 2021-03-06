# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(default='action', max_length=250)),
                ('action_header', models.CharField(default='action', max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, unique=id)),
                ('is_enable', models.BooleanField(default=True)),
                ('action_order', models.IntegerField()),
                ('templatesource', models.CharField(default='personalia/index.html', max_length=250)),
                ('query_function', models.CharField(default='GetIndex', max_length=20)),
                ('is_direct', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('menu_id', 'action_order'),
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('menu_parent', models.CharField(default='000000', max_length=6)),
                ('menu_type', models.CharField(choices=[('g', 'Group'), ('p', 'Page')], default='g', max_length=1)),
                ('menu_name', models.CharField(default='menu', max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, unique=models.CharField(max_length=6, primary_key=True, serialize=False))),
                ('is_active', models.BooleanField(default=True)),
                ('is_act_view', models.BooleanField(default=True)),
                ('menu_order', models.IntegerField()),
                ('templatesource', models.CharField(default='personalia/index.html', max_length=250)),
                ('query_function', models.CharField(default='GetIndex', max_length=20)),
            ],
            options={
                'ordering': ('menu_parent', 'menu_order'),
            },
        ),
        migrations.AddField(
            model_name='action',
            name='menu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actionMenu', to='training.Menu'),
        ),
    ]
