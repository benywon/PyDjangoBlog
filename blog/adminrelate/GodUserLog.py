# -*- coding: utf-8 -*-
import os
import datetime
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import time
import shutil
from PublicMethods.FileRelate import GetFileList, TransferFile
from PublicMethods.vdisksdk import UpdateData, UpdateFiles
from blog.models import GodUser, BackUpInfo, UserLogInfo
from django.template import loader,Context
__author__ = 'benywon'
from django.shortcuts import render, render_to_response
from django import forms
from urllib import quote_plus
IsLogin=False
import sys


class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())

class RegistForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
    email = forms.EmailField(required=False)
    pubkey=forms.CharField(label='口令：',max_length=100)


def register(request):
    message=''
    if request.method == "POST":
        uf = RegistForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            time=datetime.datetime.now()
            pubkey=uf.cleaned_data['pubkey']
            if pubkey != '7758521':#我们的口令
                uf = RegistForm()
                message="请输入口令！如果没有请向god@bingning.wang 发一封申请邮件获取！"
            else:
                #将表单写入数据库
                #要检查用户名是否存在
                if _doesUserContains(username):
                    message=username+u"已经被注册！"
                else:
                    user = GodUser()
                    user.username = username
                    user.password = password
                    if email !='' and email is not None:
                        user.email=email
                    user.timestamp=time
                    user.save()
                    #返回注册成功页面
                    return render_to_response('registsuccess.html',{'username':username})
    else:
        uf = RegistForm()
    return render_to_response('regist.html',{'uf':uf,'message':message},context_instance=RequestContext(request))

def _doesUserContains(user):
    try:
        GodUser.objects.get(username=user)
    except ObjectDoesNotExist:
        return False
    except Exception:
        return False
    return True

# def login(req):
#     username = req.COOKIES.get('username')
#     if username != '' and username is not None:
#         response = HttpResponseRedirect('/blog/god')
#         return response
#     if req.method == 'POST':
#         uf = UserForm(req.POST)
#         if uf.is_valid():
#             #获取表单用户密码
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#             #获取的表单数据与数据库进行比较
#             user = GodUser.objects.filter(username__exact = username,password__exact = password)#精确等于
#             if user:
#                 #比较成功，跳转index
#                 response = HttpResponseRedirect('/blog/god')
#                 #将username写入浏览器cookie,失效时间为3600
#                 response.set_cookie('username',username,7200)#两个小时失效
#                 return response
#             else:
#                 #比较失败，还在login
#                 return HttpResponseRedirect('/blog/login')
#     else:
#         uf = UserForm()
#     return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))
def login(req):
    username = req.COOKIES.get('username')
    if username != '' and username is not None:
        response = HttpResponseRedirect('/blog/god')
        return response
    if req.method == 'POST':
        #获取表单用户密码
        username = req.POST.get('username')
        password = req.POST.get('password')
        #获取的表单数据与数据库进行比较
        user = GodUser.objects.filter(username__exact = username,password__exact = password)#精确等于
        if user:
            #比较成功，跳转index
            response = HttpResponseRedirect('/blog/god')
            #将username写入浏览器cookie,失效时间为3600
            response.set_cookie('username',username,7200)#两个小时失效
            return response
        else:
            #比较失败，还在login
            return HttpResponseRedirect('/blog/login')
    else:
        pass

    static_html = 'loginHtml5.html'
    return render(req, static_html)

def logoutmy(req):
    response= HttpResponseRedirect('/blog/index')
    response.delete_cookie('username')
    return response


def godchange(request):
    username = request.COOKIES.get('username')
    if username == '' or username   == None:#检测是否已经登录
        return HttpResponseRedirect('/blog/login')
    else:
        if username=='god':
            isgod=True
        else:
            isgod=False
        t = loader.get_template("myadmin.html")
        c = Context({'username':username,'goduser':isgod})
        return HttpResponse(t.render(c))


def DataRestore(request):
    username = request.COOKIES.get('username')
    if username == 'god':
        if request.method == 'GET':
            string=request.GET.get('pwd', '')
            if string =='7758521':
                __storedatabase()
                return HttpResponseRedirect('/blog/index')
            elif string=='5211314':
                __storeFile()
                return HttpResponseRedirect('/blog/index')
            else:
                return render_to_response('UpdateDataBase.html')
    else:
        return HttpResponseRedirect('/blog/index')
def __storedatabase():
    path=os.path.abspath('.')
    dataname='db.sqlite3'

    ISOTIMEFORMAT='%Y-%m-%d-%H-%M-%S'
    timestr=time.strftime( ISOTIMEFORMAT, time.localtime())

    source=path+'\\'+dataname
    dest=path+'\\backupdatabase\\'+timestr+dataname
    __ourcopy(source,dest)
    UpdateData(dest)
    dataname='userlogdb.sqlite3'

    ISOTIMEFORMAT='%Y-%m-%d-%H-%M-%S'
    timestr=time.strftime( ISOTIMEFORMAT, time.localtime())

    source=path+'\\'+dataname
    dest=path+'\\backupdatabase\\'+timestr+dataname
    __ourcopy(source,dest)
    UpdateData(dest)

    dataname='Articlesdb.sqlite3'

    ISOTIMEFORMAT='%Y-%m-%d-%H-%M-%S'
    timestr=time.strftime( ISOTIMEFORMAT, time.localtime())

    source=path+'\\'+dataname
    dest=path+'\\backupdatabase\\'+timestr+dataname
    __ourcopy(source,dest)
    UpdateData(dest)
    # os.remove(dest)

def __storeFile():
    path=os.path.abspath('.')
    filelist=GetFileList(path+"\\FileDir",[])
    for myfile in filelist:
        if __doesupload(myfile):
            continue
        else:
            try:
                updateFILE(myfile)
            except:
                continue
            po=BackUpInfo()
            times=datetime.datetime.now()
            po.filename=myfile
            po.timestamp=times
            po.save()


def __getResourcesName(filename):
    return filename.decode('gbk')+'CCC'
def __doesupload(myfile):
    try:
        BackUpInfo.objects.get(filename=myfile)[0]
    except ObjectDoesNotExist:
        return False
    except Exception:
        return False
    return True

def updateFILE(myfile):
    #首先转换一下名字
    aftername=__getResourcesName(myfile)
    TransferFile(myfile,aftername)
    UpdateFiles(aftername)
    os.remove(aftername)#删除这一个临时文件

def __ourcopy(srcs,dest):
    shutil.copyfile(srcs, dest)


def EditUser(request):
    username = request.COOKIES.get('username')
    if username != 'god':#检测是否已经登录
        return HttpResponseRedirect('/blog/index')
    num=-1
    try:
        num=request.GET['id']
        num=int(num)
    except:
        num=-1
    if num>=0:
        GodUser.objects.filter(id__exact=num).delete()
    posts=GodUser.objects.all().order_by('-id')
    t=render_to_response('EditUser.html',{'posts':posts,'user':'王炳宁'},context_instance=RequestContext(request))
    return t

def GetRequestIp(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip =request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip =request.META['REMOTE_ADDR']
    return ip

def LogUserInfo(request):
    ip=GetRequestIp(request)
    cc=UserLogInfo()
    cc.Ip=ip
    username=request.COOKIES.get('username')
    if username=='' or username is None:
        username='UnKnow'
    cc.User=username
    cc.timestamp=datetime.datetime.now()
    cc.save(using='userlog')

def ShowUserLog(request):
    username = request.COOKIES.get('username')
    if username != 'god':#检测是否已经登录
        return HttpResponseRedirect('/blog/index')
    try:
        num=request.GET['p']
        num=int(num)
    except:
        num=1

    showlen=20
    #我们先来确定这个范围
    lengh=len(UserLogInfo.objects.using('userlog').all())
    if num==0:
        num=1
    if lengh<=showlen:
        start=0
        end=showlen
    else:
        start=(num-1)*showlen
        end=num*showlen
    posts=UserLogInfo.objects.using('userlog').all().order_by('-id')[start:end]
    # __transferDataBase()
    t=render_to_response('ShowUserLog.html',{'posts':posts,'number':num,'pre':num-1,'next':num+1},context_instance=RequestContext(request))
    return t

def __transferDataBase():
    post=UserLogInfo.objects.using('default').all()
    for p in post:
        p.save(using='userlog')
