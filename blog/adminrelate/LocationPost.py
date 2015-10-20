# -*- coding: utf-8 -*-
import urllib2
import re
from blog.adminrelate.GodUserLog import GetRequestIp

__author__ = 'benywon'

import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import BlogPic, UserPosition
from django.template import loader,Context
import json
from django.db.models import Q


def Location(request):
    showlen=35
    username = request.COOKIES.get('username')
    if username=='' or username is None:
        return HttpResponseRedirect('/blog/login')
    if request.method == "POST":
        lat=request.POST.get('lat')
        lng=request.POST.get('lng')
        #然后我们开始大干一场了 调用java
        time=datetime.datetime.now()
        mypos=UserPosition()
        mypos.latitude=float(lat)
        mypos.longtitude=float(lng)
        mypos.username=username
        c=GetPos(lat,lng)
        c.FindPos()
        ip=GetRequestIp(request)
        mypos.position=c.position
        mypos.timestamp=time
        mypos.Ip=ip
        mypos.save()
    if username!='god':
        q=Q(username__exact=username)
        lengh=len(UserPosition.objects.filter(q))
    else:
        q=False
        lengh=len(UserPosition.objects.all())
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
    if q is False:
        posts=UserPosition.objects.all().order_by('-id')[start:end]
    else:
        posts=UserPosition.objects.filter(q).order_by('-id')[start:end]
    #
    # t = loader.get_template("Location.html")
    # c = Context({'posts':posts,'number':num,'pre':num-1,'next':num+1})
    # return HttpResponse(t.render(c))
    return render_to_response('Location.html',{'posts':posts,'number':num,'pre':num-1,'next':num+1},context_instance=RequestContext(request))
class GetPos:
    lat=0.0
    lng=0.0
    position='北京'
    def __init__(self,lat,lng):
        self.lat=lat
        self.lng=lng

    def FindPos(self):
        content=self.__getcontent()
        m=re.match(r'renderReverse&&renderReverse\((.*)\)',content)
        dio=m.group(1)
        s=json.loads(dio)
        self.position=s["result"]["formatted_address"]
    def __getcontent(self):
        loc=self.lat+','+self.lng
        url='http://api.map.baidu.com/geocoder/v2/?ak=GgaUwOwkGZPVuAtYCjniyN4V&callback=renderReverse&location='+loc+'&output=json&pois=1'
        content = urllib2.urlopen(url).read().decode('utf-8')
        return content