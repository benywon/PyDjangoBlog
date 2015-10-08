# -*- coding: utf-8 -*-
import datetime
import json
import urllib2
from django.test import TestCase
import re
# Create your tests here.

url='http://api.map.baidu.com/geocoder/v2/?ak=GgaUwOwkGZPVuAtYCjniyN4V&callback=renderReverse&location=39.1232,116.2873&output=json&pois=1'
content =urllib2.urlopen(url).read().decode('utf-8')
m=re.match(r'renderReverse&&renderReverse\((.*)\)',content)
dio=m.group(1)
s=json.loads(dio)
location=s["result"]["formatted_address"]



