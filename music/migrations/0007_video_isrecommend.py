# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-11 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_music_isnew'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='isRecommend',
            field=models.BooleanField(default=False, verbose_name='是否要推荐'),
        ),
    ]
