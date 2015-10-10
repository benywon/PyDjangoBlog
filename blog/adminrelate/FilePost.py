# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import BlogPic, BlogFile, BackUpInfo

__author__ = 'benywon'

from django import forms


class FileForm(forms.Form):
    file = forms.FileField(label=u'文件：')


def FILE(request):
    username = request.COOKIES.get('username')
    if username == '':#检测是否已经登录
        return HttpResponseRedirect('/blog/login')
    else:
        if request.method == "POST":
            uf = FileForm(request.POST,request.FILES)
            if uf.is_valid():
                #获取表单信息
                pic = uf.cleaned_data['file']
                time=datetime.datetime.now()
                #将表单写入数据库
                picture=BlogFile()
                picture.timestamp=time
                picture.headFile=pic
                picture.save()
                return HttpResponseRedirect('/blog/index')
        else:
            uf = FileForm()
        return render_to_response('FIlePost.html',{'uf':uf},context_instance=RequestContext(request))
def EditFiles(request):
    username = request.COOKIES.get('username')
    if username != 'god':#检测是否已经登录
        return HttpResponseRedirect('/blog/index')
    showlen=30
    lengh=len(BlogFile.objects.all())
    try:
        num=request.GET['p']
        num=int(num)
    except:
        num=1

    if num==0:
        num=1
    if lengh<=showlen:
        start=0
        end=showlen
    else:
        start=(num-1)*showlen
        end=num*showlen
    posts=BlogFile.objects.all().order_by('-id')[start:end]
    t=render_to_response('EditFile.html',{'posts':posts,'user':'王炳宁','number':num,'pre':num-1,'next':num+1},context_instance=RequestContext(request))
    return t






def BackUpSee(request):
    posts=BackUpInfo.objects.all().order_by('-id')
    t=render_to_response('SeeBackUp.html',{'posts':posts,'user':'王炳宁'},context_instance=RequestContext(request))
    return t