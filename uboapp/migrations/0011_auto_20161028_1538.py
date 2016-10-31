# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uboapp', '0010_auto_20161028_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgBuilding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='uboapp/media/evil.gif', upload_to='uboapp/media/')),
            ],
        ),
        migrations.RemoveField(
            model_name='building',
            name='image',
        ),
        migrations.AddField(
            model_name='imgbuilding',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uboapp.Building'),
        ),
    ]
