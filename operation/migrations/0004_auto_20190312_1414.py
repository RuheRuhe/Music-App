# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 14:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20190311_1955'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0003_auto_20190309_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, verbose_name='评论')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='music.Video', verbose_name='评论所属视频')),
            ],
            options={
                'verbose_name': '视频评论',
                'verbose_name_plural': '视频评论',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='VideoCommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, verbose_name='评论')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='operation.VideoComment', verbose_name='二级评论')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.VideoCommentReply', verbose_name='回复对象')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
            ],
            options={
                'ordering': ['add_time'],
            },
        ),
        migrations.RemoveField(
            model_name='musiccomment',
            name='music',
        ),
        migrations.DeleteModel(
            name='MusicComment',
        ),
    ]
