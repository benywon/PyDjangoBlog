# -*- coding: utf-8 -*-
import re
import time

__author__ = 'benywon'
uu=u'我们的故事。奇偶I四点几覅哦V皇家。啊送I换掉很多 啊送id回家。奥is航道局哦回家奥是的V。'

cc=re.sub(u'。',u'。；',uu)

print(cc)