# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uboapp', '0006_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='building',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]