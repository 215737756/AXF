# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2021-04-08 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AxfFoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=32)),
                ('typename', models.CharField(max_length=32)),
                ('childtypenames', models.CharField(max_length=168)),
                ('typesort', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_foodtype',
            },
        ),
    ]
