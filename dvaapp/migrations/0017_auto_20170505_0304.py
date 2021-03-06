# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 03:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0016_auto_20170505_0142'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vlabel',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='vlabel',
            name='vdn_dataset',
        ),
        migrations.RemoveField(
            model_name='vlabel',
            name='video',
        ),
        migrations.RemoveField(
            model_name='appliedlabel',
            name='label',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='label',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='label_parent',
        ),
        migrations.AddField(
            model_name='appliedlabel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appliedlabel',
            name='scene',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Scene'),
        ),
        migrations.AddField(
            model_name='appliedlabel',
            name='source',
            field=models.CharField(choices=[('UI', 'User Interface'), ('DR', 'Directory Name'), ('AG', 'Algorithm'), ('VD', 'Visual Data Network')], default='UI', max_length=2),
        ),
        migrations.AlterField(
            model_name='appliedlabel',
            name='label_name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='VLabel',
        ),
    ]
