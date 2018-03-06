# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-06 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0076_auto_20180124_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d\u79f0')),
                ('log_info', models.CharField(max_length=1000, verbose_name='\u65e5\u5fd7\u4fe1\u606f')),
                ('result', models.CharField(max_length=200, null=True, verbose_name='\u64cd\u4f5c\u7ed3\u679c')),
                ('operation_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u64cd\u4f5c\u65f6\u95f4')),
            ],
        ),
    ]
