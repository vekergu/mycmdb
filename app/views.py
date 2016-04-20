#encoding:utf-8
from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.http.response import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.safestring import mark_safe
from django.contrib.redirects.models import Redirect
from django.template.context import RequestContext
from Cython.Compiler.Naming import args_cname
from app import models
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from django.contrib import auth
# Create your views here.
def index(request): 
    total_idc = models.Idc.objects.aggregate(Count('idc_name'))
    idc_num = total_idc["idc_name__count"]
    total_host = models.HostList.objects.aggregate(Count('hostname'))
    host_num = total_host["hostname__count"]
    #locals()返回一个包含当前作用域里面的所有变量和它们的值的字典
    return render_to_response("index.html",locals())
    #return render_to_response("index.html")
def login(request):
    return render_to_response("login.html")

def authin(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')

    total_idc =models.Idc.objects.aggregate(Count('idc_name'))
    idc_num = total_idc["idc_name__count"]
    user = auth.authenticate(username=username,password=password)
    total_host = models.HostList.objects.aggregate(Count('hostname'))
    host_num = total_host["hostname__count"]

    if user is not None:
            auth.login(request,user)
            return  render_to_response('index.html',{'login_user':request.user,'idc_num':idc_num,'host_num':host_num})
    else:
            return render_to_response('login.html',{'login_err':'Wrong username or password'})

@login_required
def idc(request):
    all_idc = models.Idc.objects.all()
    return render_to_response("idc.html",locals())

@login_required
def addidc(request):
    nameInput = request.GET['nameInput'] 
    msgInput = request.GET['msgInput'] 
    idc_add = models.Idc(idc_name=nameInput,remark=msgInput)
    idc_add.save()
    return HttpResponse('ok')

@login_required
def idc_delete(request,id=None):
    if request.method == 'GET':
        id = request.GET.get('id')
        models.Idc.objects.filter(id=id).delete()
        return HttpResponseRedirect('/idc/')
    
    
    
    
    
    