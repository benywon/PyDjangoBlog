# -*- coding: utf-8 -*-
import datetime
import random
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from blog.MyBlog.BlogSummary import GetNlp
from blog.models import PersonalDairy
from django.template import loader,Context, RequestContext

__author__ = 'benywon'

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label=u'名称：',max_length=200,required=False)
    # Description=UEditorField("描述",initial="",width=1000,height=500,max_length=10000,toolbars="full",imagePath="./FileDir/blogmaterials/uploadpic/",filePath="./FileDir/blogmaterials/uploadFile/")
    category = forms.CharField(label=u'类别：',max_length = 150,required=False)
    abstract = forms.CharField(label=u'简要介绍：',max_length = 250000,required=False)
    class Meta:
        model=PersonalDairy
        fields = ('title', 'body','category','abstract')

def ShowDairy(request):
    username=request.COOKIES.get('username')
    if username is not None and username=="god":
        pass
    else:
        return HttpResponseRedirect('/blog/login')
    showlen=20
    lengh=len(PersonalDairy.objects.using('Articles').all())
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
    posts=PersonalDairy.objects.using('Articles').all().order_by('-id')[start:end]
    for post in posts:
        post.random=random.randint(1, 4)
    t = loader.get_template("MyDairyHtml.html")
    c = Context({'posts':posts,'number':num,'pre':num-1,'next':num+1})
    return t.render(c)

def DairyContent(request):
    username = request.COOKIES.get('username')
    if not(username is not None and username=="god"):
        return HttpResponseRedirect('/blog/login')
    else:
        if request.method == "POST":
            uf = ArticleForm(request.POST)
            contentssave=PersonalDairy()

            if uf.is_valid():
                #获取表单信息
                title = uf.cleaned_data['title']
                Description = uf.cleaned_data['body']
                abstract = uf.cleaned_data['abstract']
                category = uf.cleaned_data['category']
                time=datetime.datetime.now()
                #将表单写入数据库
                if abstract is None or abstract =='':
                    c=GetNlp(Description)
                    abstract=c.summary
                article = contentssave
                article.title=title
                article.body=Description
                if username =='god':
                    article.auther=u'王炳宁'
                else:
                    article.auther=username
                if abstract is None or abstract =='':
                    c=GetNlp(Description)
                    abstract=c.summary
                #要确保summary的大小
                slen=len(abstract)
                if slen>100:
                    slen=100
                article.category=category[0:slen]
                article.abstract=abstract
                article.timestamp=time
                article.save(using='Articles')
                return HttpResponseRedirect('/blog/Dairy')
        else:
            uf = ArticleForm(instance=None)
        return render_to_response('DairyPost.html',{'uf':uf})
def DairyEdit(request):
    username = request.COOKIES.get('username')
    if username != 'god':#检测是否已经登录
        return HttpResponseRedirect('/blog/index')
    if request.method == "GET":
        showlen=20
        lengh=len(PersonalDairy.objects.using('Articles').all())
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
            PersonalDairy.objects.using('Articles').filter(id__exact=did).delete()
        if alter>=0:
            post=PersonalDairy.objects.using('Articles').get(id=alter)#要改变的
            #跳转到更改页面
            uf=ArticleForm(instance=post)
            global preeditid
            preeditid=post.id
            return render_to_response('DairyPost.html',{'uf':uf})
        posts=PersonalDairy.objects.using('Articles').all().order_by('-id')[start:end]
        t=render_to_response('EditDairy.html',{'posts':posts,'number':num,'pre':num-1,'next':num+1},context_instance=RequestContext(request))
        return t
    else:
        uf = ArticleForm(request.POST)
        if uf.is_valid():
            global preeditid
            #获取表单信息
            title = uf.cleaned_data['title']
            Description = uf.cleaned_data['body']
            abstract = uf.cleaned_data['abstract']
            if abstract is None or abstract =='':
                    c=GetNlp(Description)
                    abstract=c.summary
            category = uf.cleaned_data['category']
            time=datetime.datetime.now()
            PersonalDairy.objects.using('Articles').filter(id=preeditid).update(title=title,body=Description,abstract=abstract,category=category,lastmodified=time)

            return HttpResponseRedirect('/blog/Post/Dairy/edit')
def ShowOneDairy(request):
    username = request.COOKIES.get('username')
    if username != 'god':#检测是否已经登录
        return HttpResponseRedirect('/blog/index')
    try:
        num=request.GET['id']
        num=int(num)
    except:
        num=1
    post=PersonalDairy.objects.using('Articles').get(id=num)
    post.timestamp=post.timestamp.date()
    username = request.COOKIES.get('username')
    t = loader.get_template("Mydairy.html")
    c = Context({'post':post})
    return HttpResponse(t.render(c))
