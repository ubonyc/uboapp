# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-29 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uboapp', '0011_auto_20161229_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='client_ip',
            field=models.CharField(default='0.0.0.0', max_length=15),
        ),
    ]
