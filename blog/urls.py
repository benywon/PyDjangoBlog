# -*- coding: utf-8 -*-
import os
from blog.MyBlog.BlogContent import ShowArticle
from blog.MyBlog.MyDairy import ShowOneDairy
from blog.adminrelate import poempost
from mysites import settings

__author__ = 'benywon'
from django.conf.urls import *
from blog.views import *
from adminrelate.GodUserLog import *

urlpatterns = [
                      url(r'^about/',about),
                      url(r'^index/',index),
                      url(r'^ceshi/',ceshi),
                      url(r'^guestbook/',guestbook),
                      url(r'^diandi/',diandi),
                      url(r'^learn/$',learn),
                      url(r'^learn/?p=\d*',learn),
                      url(r'^learn/FileDir/blogmaterials/(?P<path>.*)$','django.views.static.serve',{'document_root':'FileDir/blogmaterials/'}),
                      url(r'^learn/',learn),
                      url(r'^news/',news),
                      url(r'^shuo/',shuo),
                      url(r'^Article/$',ShowArticle),
                      url(r'^Dairy/$',dairy),
                      url(r'^Dairy/?p=\d*',dairy),
                      url(r'^Article/?id=\d*',ShowArticle),
                      url(r'^MyDairy/$',ShowOneDairy),
                      url(r'^MyDairy/?id=\d*',ShowOneDairy),
                      url(r'^MyDairy/FileDir/blogmaterials/(?P<path>.*)$','django.views.static.serve',{'document_root':'FileDir/blogmaterials/'}),
                      url(r'^Article/FileDir/blogmaterials/(?P<path>.*)$','django.views.static.serve',{'document_root':'FileDir/blogmaterials/'}),
                      url(r'^xc/',xc),
                      url(r'^login/$',login,name = 'login'),
                      url(r'^login/(?P<path>.*)$','django.views.static.serve',{'document_root':'medias/'}),
                      url(r'^logout/$',logoutmy,name = 'logout'),
                      url(r'^regist/$',register,name = 'regist'),
                      url(r'^god/$',godchange,name = 'godchange'),
                      url(r'^Post/', include('blog.adminrelate.urls')),#有关更改的 都放在这
                      url(r'^video/$',video),
                      ]

