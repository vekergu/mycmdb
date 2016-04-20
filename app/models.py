#coding:utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import *
import time

class Idc(models.Model):
    idc_name = models.CharField(max_length=40, verbose_name=u'机房名称')
    remark = models.CharField(max_length=40, verbose_name=u'备注')
    def __unicode__(self):
        return self.idc_name
    class Meta:
        verbose_name = u'机房列表'
        verbose_name_plural = u'机房列表'    

class HostList(models.Model):
    ip = models.GenericIPAddressField(unique=True, verbose_name=u'IP地址')
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    group = models.ManyToManyField('Group', null=True, blank=True ,verbose_name=u'组名') 
    application = models.CharField(max_length=20, verbose_name=u'应用')
    bianhao = models.CharField(max_length=30, verbose_name=u'编号') 
    idc_name = models.CharField(max_length=40,null=True,blank=True, verbose_name=u'所属机房') 
    def __unicode__(self):
        return self.ip
    class Meta:
        verbose_name = u'主机列表'
        verbose_name_plural = u'主机列表'
        
class Group(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'主机组信息'
        verbose_name_plural = u'主机组信息管理'