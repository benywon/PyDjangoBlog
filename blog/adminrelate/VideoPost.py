# -*- coding: utf-8 -*-
from PublicMethods.CheckLog import checkLogin

__author__ = 'benywon'
__time__ = '2015-10-10-20:46'
__contact__ = 'god@bingning.wang'

import datetime
from blog.adminrelate import PicPost
from blog.models import BlogVideo
from django.db.models import Q
from django import forms
from django.shortcuts import render
from django.template import loader,Context


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


class VideoForm(forms.Form):
    video=forms.FileField(label=u'视频')
    ishow = forms.ChoiceField(label=u'是否公开',choices=PicPost.SOURCES_CHOICES)
    description = forms.CharField(label=u'介绍：',max_length=200,required=False)


def VideoPo(request):
    username = request.COOKIES.get('username')
    if username == '' or username is None:#检测是否已经登录
        return HttpResponseRedirect('/blog/login')
    else:
        if request.method == "POST":
            uf = VideoForm(request.POST,request.FILES)
            if uf.is_valid():
                #获取表单信息
                videoform = uf.cleaned_data['video']
                ishow = uf.cleaned_data['ishow']
                description = uf.cleaned_data['description']
                time=datetime.datetime.now()
                #将表单写入数据库
                video = BlogVideo()
                if ishow==u'True':
                    video.isshow=True
                else:
                    video.isshow=False
                video.user=username
                video.timestamp=time
                video.description=description
                video.video=videoform
                video.save()
                return HttpResponseRedirect('/blog/video')
        else:
            uf = VideoForm()
        return render_to_response('VideoPost.html',{'uf':uf},context_instance=RequestContext(request))

def ShowVideo(request):
    showlen=10
    lengh=len(BlogVideo.objects.all())
    username = request.COOKIES.get('username')
    if username == '' or username is None:#检测是否已经登录
        return HttpResponseRedirect('/blog/login')
    try:
        num=request.GET['p']
        num=int(num)
    except:
        num=1
    #我们先来确定这个范围
    if num==0:
        num=1
    if lengh<=showlen:
        start=0
        end=showlen
    else:
        start=(num-1)*showlen
        end=num*showlen
    if username == 'god':
        posts=BlogVideo.objects.all().order_by('-id')[start:end]
    else:
        posts=BlogVideo.objects.filter(Q(isshow__exact=True)|Q(user=username)).order_by('-id')[start:end]

    IsLogin=checkLogin(request)
    t = loader.get_template("VideoShow.html")
    c = Context({'posts':posts,'number':num,'pre':num-1,'next':num+1,'IsLogin':IsLogin})
    return HttpResponse(t.render(c))

def EditVideo(request):
    username = request.COOKIES.get('username')
    if username != 'god':#检测是否已经登录
        return HttpResponseRedirect('/blog/index')
    showlen=10
    lengh=len(BlogVideo.objects.all())
    num=-1
    try:
        did=request.GET['id']
        did=int(did)
    except:
        did=-1
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
    if did>=0:
        BlogVideo.objects.filter(id__exact=did).delete()
    posts=BlogVideo.objects.all().order_by('-id')[start:end]
    t=render_to_response('EditVideo.html',{'posts':posts,'number':num,'pre':num-1,'next':num+1},context_instance=RequestContext(request))
    return t