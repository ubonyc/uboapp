# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-29 05:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uboapp', '0010_auto_20161204_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='five',
        ),
        migrations.RemoveField(
            model_name='building',
            name='four',
        ),
        migrations.RemoveField(
            model_name='building',
            name='one',
        ),
        migrations.RemoveField(
            model_name='building',
            name='three',
        ),
        migrations.RemoveField(
            model_name='building',
            name='two',
        ),
    ]
