# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closetApp', '0003_auto_20170211_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=b'mal', max_length=128),
        ),
        migrations.AlterField(
            model_name='clothingtype',
            name='pos_x',
            field=models.IntegerField(verbose_name=1),
        ),
        migrations.AlterField(
            model_name='clothingtype',
            name='pos_y',
            field=models.IntegerField(verbose_name=1),
        ),
    ]
