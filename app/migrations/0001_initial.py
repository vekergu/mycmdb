# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u7ec4\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u7ec4\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='HostList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField(unique=True, verbose_name='IP\u5730\u5740')),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('application', models.CharField(max_length=20, verbose_name='\u5e94\u7528')),
                ('bianhao', models.CharField(max_length=30, verbose_name='\u7f16\u53f7')),
                ('idc_name', models.CharField(max_length=40, null=True, verbose_name='\u6240\u5c5e\u673a\u623f', blank=True)),
                ('group', models.ManyToManyField(to='app.Group', null=True, verbose_name='\u7ec4\u540d', blank=True)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u5217\u8868',
                'verbose_name_plural': '\u4e3b\u673a\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idc_name', models.CharField(max_length=40, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('remark', models.CharField(max_length=40, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u673a\u623f\u5217\u8868',
                'verbose_name_plural': '\u673a\u623f\u5217\u8868',
            },
        ),
    ]
