# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20190312_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocommentreply',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='videocommentreply',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='videocommentreply',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='videocomment',
            options={'verbose_name': '视频评论', 'verbose_name_plural': '视频评论'},
        ),
        migrations.RemoveField(
            model_name='videocomment',
            name='content',
        ),
        migrations.RemoveField(
            model_name='videocomment',
            name='user',
        ),
        migrations.AddField(
            model_name='videocomment',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='用户邮箱'),
        ),
        migrations.AddField(
            model_name='videocomment',
            name='name',
            field=models.CharField(default='', max_length=32, verbose_name='评论者'),
        ),
        migrations.AddField(
            model_name='videocomment',
            name='text',
            field=models.TextField(default='', verbose_name='评论'),
        ),
        migrations.AlterField(
            model_name='videocomment',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='videocomment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Video', verbose_name='评论所属的视频'),
        ),
        migrations.DeleteModel(
            name='VideoCommentReply',
        ),
    ]
