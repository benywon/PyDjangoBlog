# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.MyBlog import BlogContent
from blog.adminrelate import TweetPost,poempost,PicPost,CommentPost,GodUserLog

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
    return render(request, static_html)

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

def poem(request):
    static_html = 'xc.html'
    return render(request, static_html)


def poem(request):
    static_html = 'xc.html'
    return render(request, static_html)