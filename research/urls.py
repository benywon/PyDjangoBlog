# -*- coding: utf-8 -*-
from research.views import index

__author__ = 'benywon'
__time__ = '2015-10-20-22:24'
__contact__ = 'god@bingning.wang'
from django.conf.urls import *
urlpatterns = [
                      url(r'^index/',index),
                      ]
