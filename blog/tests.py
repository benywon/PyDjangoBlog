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
    regx=r'<img.*src="(.*?)"'
    m=re.search(regx,instr)
    if m:
        return True,m.group(0)
    else:
        return False

instar='<h1 label="Title left" name="tl" style="border-bottom-color: rgb(204, 204, 204); border-bottom-width: 2px; border-bottom-style: solid; padding: 0px 4px 0px 0px; margin: 0px 0px 10px; text-align: center;"><span style="color:#e36c09;">[我们的 哥哥]</span></h1><p><span style="color:#e36c09;"><br/></span></p><table width="100%" border="1" bordercolor="#95B3D7" style="border-collapse:collapse;"><tbody><tr class="firstRow"><td width="200" style="text-align:center;" class="ue_t">【此处插入照片】</td><td><p><br/></p><p>联系电话：<span class="ue_t">[键入您的电话]</span></p><p><br/></p><p>电子邮件：<span class="ue_t">[键入您的电子邮件地址]</span></p><p><br/></p><p>家庭住址：<span class="ue_t">[键入您的地址]</span></p><p><br/></p></td></tr></tbody></table><h3><span style="color:#e36c09;font-size:20px;">目标职位</span></h3><p style="text-indent:2em;" class="ue_t">[此处键入您的期望职位]</p><h3><span style="color:#e36c09;font-size:20px;">学历</span></h3><p></p><ol style="list-style-type: decimal;" class=" list-paddingleft-2"><li><p><span class="ue_t">[键入起止时间]</span> <span class="ue_t">[键入学校名称] </span> <span class="ue_t">[键入所学专业]</span> <span class="ue_t">[键入所获学位]</span></p></li><li><p><span class="ue_t">[键入起止时间]</span> <span class="ue_t">[键入学校名称]</span> <span class="ue_t">[键入所学专业]</span> <span class="ue_t">[键入所获学位]</span></p></li></ol><h3><span style="color:#e36c09;font-size:20px;" class="ue_t">工作经验</span></h3><ol style="list-style-type: decimal;" class=" list-paddingleft-2"><li><p><span class="ue_t">[键入起止时间]</span> <span class="ue_t">[键入公司名称]</span> <span class="ue_t">[键入职位名称]</span></p></li><ol style="list-style-type: lower-alpha;" class=" list-paddingleft-2"><li><p><span class="ue_t">[键入负责项目]</span> <span class="ue_t">[键入项目简介]</span></p></li><li><p><span class="ue_t">[键入负责项目]</span> <span class="ue_t">[键入项目简介]</span></p></li></ol><li><p><span class="ue_t">[键入起止时间]</span> <span class="ue_t">[键入公司名称]</span> <span class="ue_t">[键入职位名称]</span></p></li><ol style="list-style-type: lower-alpha;" class=" list-paddingleft-2"><li><p><span class="ue_t">[键入负责项目]</span> <span class="ue_t">[键入项目简介]<img src="./FileDir/blogmaterials/uploadpic/Koala_20151009014450_280.jpg" title="" alt="Koala.jpg" width="698" height="369" style="width: 698px; height: 369px;"/></span></p></li></ol></ol><p><span style="color:#e36c09;font-size:20px;">掌握技能</span></p><p style="text-indent:2em;">&nbsp;<span class="ue_t">[这里可以键入您所掌握的技能]</span><br/></p><p><br/></p>'
isd,cc=__findAnav(instar)
print(cc)


