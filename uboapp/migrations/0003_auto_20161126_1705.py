# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 22:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uboapp', '0002_auto_20161126_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='tri',
        ),
    ]
