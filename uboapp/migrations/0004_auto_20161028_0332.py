# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uboapp', '0003_building_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='image',
            field=models.ImageField(default='uboapp/media/world.jpg', upload_to='uboapp/media/'),
        ),
    ]
