# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uboapp', '0002_auto_20161021_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='image',
            field=models.ImageField(default='media/world.jpg', upload_to='media/'),
        ),
    ]
