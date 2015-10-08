# -*- coding: utf-8 -*-
import datetime
import json
import urllib2
from django.test import TestCase
import re
# Create your tests here.
#
# url='http://api.map.baidu.com/geocoder/v2/?ak=GgaUwOwkGZPVuAtYCjniyN4V&callback=renderReverse&location=39.1232,116.2873&output=json&pois=1'
# content =urllib2.urlopen(url).read().decode('utf-8')
# m=re.match(r'renderReverse&&renderReverse\((.*)\)',content)
# dio=m.group(1)
# s=json.loads(dio)
# location=s["result"]["formatted_address"]
def __findAnav(instr):
    regx=r'<img .* src="(.*?)"'
    m=re.search(regx,instr)
    if m:
        return True,m.group(0)
    else:
        return False

instar='<p>色如果为若干热发改委如果稳如狗<img width="530" height="340" src="http://api.map.baidu.com/staticimage?center=116.404,39.915&zoom=10&width=530&height=340&markers=116.404,39.915"/><img src="./FileDir/blogmaterials/uploadpic/Jellyfish_20151008223201_954.jpg" title="" alt="Jellyfish.jpg"/></p>'
isd,cc=__findAnav(instar)
print(cc)


