# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-09 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('key', models.CharField(max_length=50)),
                ('val', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
