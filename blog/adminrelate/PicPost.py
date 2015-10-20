# -*- coding: utf-8 -*-
from StringIO import StringIO
import datetime
import os
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models.fields.files import ImageFieldFile
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import re
from PublicMethods.CheckLog import checkLogin
from blog.models import BlogPic
from django.template import loader,Context
from django.db.models import Q


__author__ = 'benywon'

from django import forms

showlen=24

SOURCES_CHOICES = (
                  (True, '公开'),
                  (False, '不公开'),
                  )

class PicForm(forms.Form):
    pic = forms.ImageField(label=u'照片：')
    title = forms.CharField(label=u'描述',max_length=300,required=False,widget=forms.Textarea(attrs={'style':"height:51px;width:249px"}))
    ishow = forms.ChoiceField(label=u'是否公开',choices=SOURCES_CHOICES)


def Pic(request):
    username = request.COOKIES.get('username')
    if username == '' or username ==None:#检测是否已经登录
        return HttpResponseRedirect('/blog/login')
    else:
        if request.method == "POST":
            uf = PicForm(request.POST,request.FILES)
            if uf.is_valid():
                #获取表单信息
                pic = uf.cleaned_data['pic']
                title = uf.cleaned_data['title']
                ishow = uf.cleaned_data['ishow']
                time=datetime.datetime.now()
                #将表单写入数据库
                picture=BlogPic()
                if ishow==u'True':
                    picture.isshow=True
                else:
                    picture.isshow=False
                picture.timestamp=time
                picture.username=username
                picture.headImg=pic
                picture.title=title
                picture.save()
                return HttpResponseRedirect('/blog/xc')
        else:
            uf = PicForm()
        return render_to_response('PicPost.html',{'uf':uf},context_instance=RequestContext(request))

def ShowPic(request):
    lengh=len(BlogPic.objects.all())
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
        posts=BlogPic.objects.all().order_by('-id')[start:end]
    else:
        posts=BlogPic.objects.filter(Q(isshow__exact=True)|Q(username=username)).order_by('-id')[start:end]

    IsLogin=checkLogin(request)
    t = loader.get_template("xc.html")
    c = Context({'posts':posts,'number':num,'pre':num-1,'next':num+1,'IsLogin':IsLogin})
    return t.render(c)

def EditPic(request):
    username = request.COOKIES.get('username')
    if username != 'god':#检测是否已经登录
        return HttpResponseRedirect('/blog/index')
    showlen=10
    lengh=len(BlogPic.objects.all())
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
        BlogPic.objects.filter(id__exact=did).delete()
    posts=BlogPic.objects.all().order_by('-id')[start:end]
    t=render_to_response('EditPic.html',{'posts':posts,'number':num,'pre':num-1,'next':num+1},context_instance=RequestContext(request))
    return t

def __myeditpreviouspic():
    BlogPic.objects.all().update(isshow=True)

#############################################################
def makeThumb(pic):
    base, ext = os.path.splitext(os.path.basename('./FileDir/Thumb/'+pic.name))
    thumb_pixbuf = make_thumb_img(os.path.join('./FileDir/Thumb', pic.name))
    relate_thumb_path = os.path.join('/Thumb', base + '.thumb' + ext)
    thumb_path = os.path.join('./FileDir', relate_thumb_path)
    thumb_pixbuf.save(thumb_path)
    thumb = ImageFieldFile(relate_thumb_path)
    return thumb

def make_thumb_img(path, size = 480):
    """处理缩略图的方法"""
    pixbuf = Image.open(path)
    width, height = pixbuf.size

    if width > size:
        delta = width / size
        height = int(height / delta)
        pixbuf.thumbnail((size, height), Image.ANTIALIAS)
        return pixbuf
def alterthumb():
    cc=BlogPic.objects.all()
    for img in cc:
        image = Image.open(img.headImg)
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')
        thumb_size=(178,200)
        image.thumbnail(thumb_size, Image.ANTIALIAS)
        outfilepath=img.headImg.name.replace('Image','Thumb')

        relate_thumb_path=outfilepath+'thumb.png'
        image.save(relate_thumb_path)
        BlogPic.objects.filter(id__exact=img.id).update(thumb=relate_thumb_path)
