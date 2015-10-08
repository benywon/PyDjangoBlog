# -*- coding: utf-8 -*-
import datetime
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import BlogComment
from django.template import loader,Context

__author__ = 'benywon'


showlen=5


def ShowComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        yourname=request.POST.get('name')
        if yourname=='':
            yourname='匿名'
        canshow=request.POST.get('canshow')
        time=datetime.datetime.now()
        if canshow=='True':
            canshow=True
        else:
            canshow=False
        mycomment=BlogComment()
        mycomment.comments=comment
        mycomment.canshow=canshow
        mycomment.name=yourname
        mycomment.timestamp=time
        mycomment.save()
    lengh=len(BlogComment.objects.all())
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
    username = request.COOKIES.get('username')
    if username == 'god':
        posts=BlogComment.objects.all().order_by('-id')[start:end]
    else:
        posts=BlogComment.objects.filter(canshow__exact=True).order_by('-id')[start:end]
    t = loader.get_template("guestbook.html")
    c = Context({'posts':posts,'number':num,'pre':num-1,'next':num+1})
    return t.render(c)

def EditComments(request):
    num=-1
    try:
        num=request.GET['id']
        num=int(num)
    except:
        num=-1
    if num>=0:
        BlogComment.objects.filter(id__exact=num).delete()
    posts=BlogComment.objects.all().order_by('-id')
    t=render_to_response('EditComments.html',{'posts':posts,'user':'王炳宁'},context_instance=RequestContext(request))
    return t