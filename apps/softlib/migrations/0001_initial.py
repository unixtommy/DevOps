# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soft',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('soft_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Softlib',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('soft_version', models.CharField(max_length=10)),
                ('soft_md5', models.CharField(max_length=100)),
                ('soft_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softlib.Soft')),
            ],
        ),
    ]