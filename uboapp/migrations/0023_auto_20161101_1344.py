# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uboapp', '0022_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]