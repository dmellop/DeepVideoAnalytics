# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0014_auto_20170405_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='parent_frame_index',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='detection',
            name='parent_frame_index',
            field=models.IntegerField(default=-1),
        ),
    ]
