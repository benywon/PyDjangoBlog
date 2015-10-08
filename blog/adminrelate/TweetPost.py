# -*- coding: utf-8 -*-
from django import forms

from django.shortcuts import render
from django.template import loader,Context


from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import GodTweet
import datetime

showlen=20

__author__ = 'benywon'
class TweetForm(forms.Form):
    tweet=forms.CharField(label='今天的心情',widget=forms.Textarea,max_length=300)
    pos = forms.CharField(label='位置',max_length=100)

def Tweet(request):
    username = request.COOKIES.get('username')
    if username == '' or username is None:#检测是否已经登录
        return HttpResponseRedirect('/blog/login')
    else:
        if request.method == "POST":
            uf = TweetForm(request.POST)
            if uf.is_valid():
                #获取表单信息
                tweets = uf.cleaned_data['tweet']
                pos = uf.cleaned_data['pos']
                time=datetime.datetime.now()
                #将表单写入数据库
                tweet = GodTweet()
                tweet.username=username
                tweet.timestamp=time
                tweet.tweet=tweets
                tweet.pos=pos
                tweet.save()
                return HttpResponseRedirect('/blog/diandi')
        else:
            uf = TweetForm()
        return render_to_response('TweetPost.html',{'uf':uf},context_instance=RequestContext(request))

def ShowTweet(request):
    lengh=len(GodTweet.objects.all())
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
    posts=GodTweet.objects.all().order_by('-id')[start:end]
    for post in posts:
        numb=len(post.tweet.encode('utf-8'))
        if numb<110:
           post.shownumber=range(5)
        elif numb<200:
            post.shownumber=range(4)
        elif numb<300:
            post.shownumber=range(3)
        elif numb<406:
            post.shownumber=range(2)
        elif numb<500:
            post.shownumber=range(1)
        else:
            post.shownumber=False
    t = loader.get_template("riji.html")
    c = Context({'posts':posts,'number':num,'pre':num-1,'next':num+1,})
    return t.render(c)


def EditTweet(request):
    username = request.COOKIES.get('username')
    if username != 'god':#检测是否已经登录
        return HttpResponseRedirect('/blog/index')
    num=-1
    try:
        did=request.GET['id']
        did=int(did)
    except:
        did=-1
    lengh=len(GodTweet.objects.all())
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
    if did>=0:
        GodTweet.objects.filter(id__exact=did).delete()
    posts=GodTweet.objects.all().order_by('-id')[start:end]
    t=render_to_response('EditTweet.html',{'posts':posts,'user':'王炳宁','number':num,'pre':num-1,'next':num+1},context_instance=RequestContext(request))
    return t

def __removeprevioustweet():
    GodTweet.objects.all().delete()