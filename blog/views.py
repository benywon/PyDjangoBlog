# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.MyBlog import BlogContent
from blog.adminrelate import TweetPost,poempost,PicPost,CommentPost,GodUserLog,VideoPost
from PublicMethods import CheckLog

from blog.models import *


# Create your views here.
def archive(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))

def about(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("about.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))

def index(request):
    static_html = 'index.html'
    GodUserLog.LogUserInfo(request)
    t = loader.get_template(static_html)
    IsLogin=CheckLog.checkLogin(request)
    c = Context({'IsLogin':IsLogin})
    return HttpResponse(t.render(c))

def shuo(request):
    t=poempost.ShowPoem(request)
    return HttpResponse(t)

def ceshi(request):
    static_html = 'ceshi.html'
    return render(request, static_html)

def guestbook(request):
    ret= CommentPost.ShowComment(request)
    return HttpResponse(ret)
def diandi(request):
    ret= TweetPost.ShowTweet(request)
    return HttpResponse(ret)
def learn(request):
    ret= BlogContent.ShowBlog(request)
    return HttpResponse(ret)

def news(request):
    static_html = 'news.html'
    return render(request, static_html)

def xc(request):
    ret= PicPost.ShowPic(request)
    return HttpResponse(ret)
def video(request):
    ret= VideoPost.ShowVideo(request)
    return ret
