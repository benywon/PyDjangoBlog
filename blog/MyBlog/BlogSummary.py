# -*- coding: utf-8 -*-
__author__ = 'benywon'
__time__ = '2015-10-20-16:08'
__contact__ = 'god@bingning.wang'

import os

jarfilepath='C:\\Users\\benywon\\IdeaProjects\\mynlptest\\out\\artifacts\\mynlptest_jar\\mynlptest.jar'

class GetNlp():
    keywords=[]
    summary=''
    content=''
    def __init__(self,content):
        self.content=content
        file_object = open('C:\\myblogtemp.txt', 'w')
        file_object.write(content.encode('utf-8'))
        file_object.close()
        self.__getkeywords()
        self.__getsummary()
    def __getkeywords(self):
        cmd='java -jar '+jarfilepath+' keywords C:\\myblogtemp.txt'
        a=os.popen(cmd).read().decode('gbk')
        cc=a.split(u'㊣')
        for c in cc:
            if c !='':
                self.keywords.append(c)
    def __getsummary(self):
        cmd='java -jar '+jarfilepath+' summary C:\\myblogtemp.txt'
        a=os.popen(cmd).read().decode('gbk')
        cc=a.split(u'㊣')
        for c in cc:
            if c !='':
                self.summary+=c+','








