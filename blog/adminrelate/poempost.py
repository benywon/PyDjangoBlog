# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from PublicMethods.CheckLog import checkLogin
from blog.models import BlogPoem
from django.template import loader,Context
from django import forms
from PublicMethods import *
import time
import re


__author__ = 'benywon'

showlen=15
preeditid=-1
SOURCES_CHOICES = (
                  (False, '不是以前的词'),
                  (True, '是以前的词'),
                  )
class PoemForm(forms.Form):
    title = forms.CharField(label=u'词牌名',max_length=100,widget=forms.TextInput(attrs={'size':30}))
    nav = forms.CharField(label=u'叙述',max_length=200,required=False,widget=forms.Textarea(attrs={'style':"height:51px;width:249px"}))
    poem=forms.CharField(label=u'诗歌',widget=forms.Textarea(attrs={'style':"height:200px;width:849px"}),max_length=1200)
    isprevious = forms.ChoiceField(label=u'是否是以前',choices=SOURCES_CHOICES)
class PoemFormModel(forms.ModelForm):
    title = forms.CharField(label=u'词牌名',max_length=100,widget=forms.TextInput(attrs={'size':30}))
    nav = forms.CharField(label=u'叙述',max_length=200,required=False,widget=forms.Textarea(attrs={'style':"height:51px;width:249px"}))
    # poem=forms.CharField(label=u'诗歌',widget=forms.Textarea(attrs={'style':"height:200px;width:849px"}),max_length=1200)
    isprevious = forms.ChoiceField(label=u'是否是以前',choices=SOURCES_CHOICES)
    class Meta:
        model=BlogPoem
        fields = ('title', 'nav','body','isprevious')
def Poem(request):
    username = request.COOKIES.get('username')
    if username == '':#检测是否已经登录
        return HttpResponseRedirect('/blog/login')
    else:
        if request.method == "POST":
            uf = PoemForm(request.POST)
            if uf.is_valid():
                #获取表单信息
                title = uf.cleaned_data['title']
                poemstr = uf.cleaned_data['poem']
                nav = uf.cleaned_data['nav']
                isprevious = uf.cleaned_data['isprevious']
                time=datetime.datetime.now()
                #将表单写入数据库
                poem = BlogPoem()
                poem.auther='王炳宁'
                poem.body=poemstr
                poem.nav=nav
                if isprevious==u'True':
                    poem.isprevious=True
                else:
                    poem.isprevious=False
                poem.title=title
                poem.timestamp=time
                poem.save()
                return HttpResponseRedirect('/blog/shuo')
        else:
            uf = PoemForm()
        return render_to_response('PoemPost.html',{'uf':uf},context_instance=RequestContext(request))

def ShowPoem(request):
    lengh=len(BlogPoem.objects.all())
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
    posts=BlogPoem.objects.all().order_by('-id')[start:end]
    for po in posts:
        pre=po.body.encode("utf-8")
        prestr=__getdiv(pre)
        div=u"；".encode('utf-8')
        po.k=prestr.split(div)
    IsLogin=checkLogin(request)
    t = loader.get_template("shuo.html")
    c = Context({'poems':posts,'number':num,'pre':num-1,'next':num+1,'IsLogin':IsLogin})
    return t.render(c)

def EditPoem(request):
    username = request.COOKIES.get('username')
    if username != 'god':#检测是否已经登录
        return HttpResponseRedirect('/blog/index')
    if request.method == "GET":
        num=-1
        try:
            num=request.GET['id']
            num=int(num)
        except:
            num=-1
        try:
            alter=request.GET['aid']
            alter=int(alter)
        except:
            alter=-1
        if num>=0:
            BlogPoem.objects.filter(id__exact=num).delete()
        if alter>=0:
            post=BlogPoem.objects.get(id=alter)#要改变的
            global preeditid
            preeditid=post.id
            uf = PoemFormModel(instance=post)
            return render_to_response('PoemPost.html',{'uf':uf})
        posts=BlogPoem.objects.all().order_by('-id')
        t=render_to_response('EditPoem.html',{'posts':posts,'user':'王炳宁'},context_instance=RequestContext(request))
        return t
    else:
        uf = PoemFormModel(request.POST)
        if uf.is_valid():
            global preeditid
            #获取表单信息
            title = uf.cleaned_data['title']
            nav = uf.cleaned_data['nav']
            body = uf.cleaned_data['body']
            isprevious=uf.cleaned_data['isprevious']
            if isprevious==u'True':
                isprevious=True
            else:
                isprevious=False
            BlogPoem.objects.filter(id=preeditid).update(title=title,nav=nav,body=body,isprevious=isprevious)
            return HttpResponseRedirect('/blog/shuo')
        else:
            return HttpResponseRedirect('/blog/index')
def __getdiv(instr):
    regx='。|！'
    afters='。；'
    out=re.sub(regx,afters,instr)
    return out
def __myeditpreviouspoem():
    """将以前的文章都改为特定时间"""
    BlogPoem.objects.all().update(isprevious=True)



