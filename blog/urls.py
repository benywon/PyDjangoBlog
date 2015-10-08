# -*- coding: utf-8 -*-
import os
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
                      url(r'^learn/',learn),
                      url(r'^news/',news),
                      url(r'^shuo/',shuo),
                      url(r'^xc/',xc),
                      url(r'^poem/',poem),
                      url(r'^login/$',login,name = 'login'),
                      url(r'^logout/$',logoutmy,name = 'logout'),
                      url(r'^regist/$',register,name = 'regist'),
                      url(r'^god/$',godchange,name = 'godchange'),
                      url(r'^Post/', include('blog.adminrelate.urls')),#有关更改的 都放在这
                      ]

