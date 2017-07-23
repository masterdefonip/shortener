# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-23 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLShortcut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Adres URL')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
