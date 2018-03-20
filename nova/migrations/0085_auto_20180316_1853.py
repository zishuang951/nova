# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-16 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0084_auto_20180316_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='date_added',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='assetgroup',
            name='comment',
            field=models.CharField(blank=True, max_length=160, null=True, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='assetgroup',
            name='name',
            field=models.CharField(max_length=80, unique=True, verbose_name='\u4e3b\u673a\u7ec4\u540d\u79f0'),
        ),
    ]