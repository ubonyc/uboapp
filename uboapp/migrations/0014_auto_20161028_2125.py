# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uboapp', '0013_auto_20161028_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgbuilding',
            name='image',
            field=models.ImageField(default='media/evil.gif', upload_to='uboapp/media/'),
        ),
    ]
