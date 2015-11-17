# -*- coding: utf-8 -*-
import base64
import hashlib
import re
import time

__author__ = 'benywon'
filename='M:/bingning.wangweb/win7web/mysites/FileDir/blogmaterials/uploadFile/最近一周的工作总结-王炳宁_20151009023659_650.doc'
inchars=bytearray(filename)
afterchars=[]
for inchar in inchars:
    afterchars.append(hex(int(inchar)))


print(str(afterchars))
