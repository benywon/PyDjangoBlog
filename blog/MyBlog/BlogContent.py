# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import re
from blog.models import  BlogsPost
from django.template import loader,Context
__author__ = 'benywon'

from django import forms
from  DjangoUeditor.forms import UEditorField


preeditid=-1

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label=u'名称：',max_length=200,required=False)
    # Description=UEditorField("描述",initial="",width=1000,height=500,max_length=10000,toolbars="full",imagePath="./FileDir/blogmaterials/uploadpic/",filePath="./FileDir/blogmaterials/uploadFile/")
    category = forms.CharField(label=u'类别：',max_length = 150,required=False)
    abstract = forms.CharField(label=u'简要介绍：',max_length = 250,required=False)
    class Meta:
        model=BlogsPost
        fields = ('title', 'body','category','abstract')




def Article(request):
    username = request.COOKIES.get('username')
    if username == '' or username is None:#检测是否已经登录
        return HttpResponseRedirect('/blog/login')
    else:
        if request.method == "POST":
            uf = ArticleForm(request.POST)
            if uf.is_valid():
                #获取表单信息
                title = uf.cleaned_data['title']
                Description = uf.cleaned_data['body']
                abstract = uf.cleaned_data['abstract']
                category = uf.cleaned_data['category']
                time=datetime.datetime.now()
                #将表单写入数据库
                article = BlogsPost()
                article.title=title
                article.body=Description
                if username =='god':
                    article.auther=u'王炳宁'
                else:
                    article.auther=username

                article.category=category
                article.abstract=abstract
                article.timestamp=time
                article.save(using='Articles')
                return HttpResponseRedirect('/blog/learn')
        else:
            uf = ArticleForm(instance=None)
        return render_to_response('ArticlePost.html',{'uf':uf})


def ShowBlog(request):
    showlen=10
    lengh=len(BlogsPost.objects.using('Articles').all())
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
    posts=BlogsPost.objects.using('Articles').all().order_by('-id')[start:end]
    for post in posts:
        [post.ishowpic,post.picshow]=__findAnav(post.body)


    t = loader.get_template("learn.html")
    c = Context({'posts':posts,'number':num,'pre':num-1,'next':num+1,})
    return t.render(c)


def __findAnav(instr):
    regx=r'<img.*src="(.*?)"'
    m=re.search(regx,instr)
    if m:
        return [True,m.group(1)]
    else:
        return [False,None]

def ShowArticle(request):
    try:
        num=request.GET['id']
        num=int(num)
    except:
        num=1
    post=BlogsPost.objects.using('Articles').get(id=num)
    post.timestamp=post.timestamp.date()
    t = loader.get_template("Article.html")
    c = Context({'post':post})
    return HttpResponse(t.render(c))


def ArticleEdit(request):
    username = request.COOKIES.get('username')
    if username != 'god':#检测是否已经登录
        return HttpResponseRedirect('/blog/index')
    if request.method == "GET":
        showlen=20
        lengh=len(BlogsPost.objects.using('Articles').all())
        num=-1
        try:
            did=request.GET['id']
            did=int(did)
        except:
            did=-1
        try:
            alter=request.GET['aid']
            alter=int(alter)
        except:
            alter=-1
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
            BlogsPost.objects.using('Articles').filter(id__exact=did).delete()
        if alter>=0:
            post=BlogsPost.objects.using('Articles').get(id=alter)#要改变的
            #跳转到更改页面
            uf=ArticleForm(instance=post)
            global preeditid
            preeditid=post.id
            return render_to_response('ArticlePost.html',{'uf':uf})
        posts=BlogsPost.objects.using('Articles').all().order_by('-id')[start:end]
        t=render_to_response('EditArticle.html',{'posts':posts,'number':num,'pre':num-1,'next':num+1},context_instance=RequestContext(request))
        return t
    else:
        uf = ArticleForm(request.POST)
        if uf.is_valid():
            global preeditid
            #获取表单信息
            title = uf.cleaned_data['title']
            Description = uf.cleaned_data['body']
            abstract = uf.cleaned_data['abstract']
            category = uf.cleaned_data['category']
            time=datetime.datetime.now()
            BlogsPost.objects.using('Articles').filter(id=preeditid).update(title=title,body=Description,abstract=abstract,category=category,lastmodified=time)

            return HttpResponseRedirect('/blog/Post/Article/edit')

