# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uboapp', '0006_auto_20161028_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='image',
            field=models.ImageField(default='uboapp/media/world.jpg', upload_to='uboapp/media/'),
        ),
        migrations.AlterField(
            model_name='building',
            name='streetname',
            field=models.CharField(db_index=True, default=0, max_length=200),
        ),
    ]