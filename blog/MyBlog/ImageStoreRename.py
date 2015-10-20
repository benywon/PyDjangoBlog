# -*- coding: utf-8 -*-
import hashlib

__author__ = 'benywon'
from django.core.files.storage import FileSystemStorage
class ImageStorage(FileSystemStorage):
    from django.conf import settings

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        #初始化
        super(ImageStorage, self).__init__(location, base_url)

    #重写 _save方法
    def _save(self, name, content):
        import os, time, random
        #文件扩展名
        ext = os.path.splitext(name)[1]
        basename=os.path.splitext(name)[0]
        #文件目录
        d = os.path.dirname(name)
        #定义文件名，年月日时分秒随机数
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '%d' % random.randint(0,1000)
        hashs=hashlib.md5(fn).hexdigest()
        #重写合成文件名
        if selffilter(ext):
            name = os.path.join(d, basename+'_'+hashs + ext)
        else:
            pass
        #调用父类方法
        return super(ImageStorage, self)._save(name, content)
def selffilter(ors):
    baseimgfile=[u'.jpg',u'.jpeg',u'.jpg',u'.png',u'.bmp',u'.gif',u'.ico',u'.tif',u'.tga',u'.pcx']
    basevideofile=[u'.mp4',u'.flv',u'.rmvb',u'.3gp',u'.avi',u'.wmv',u'.mkv',u'.mpg',u'.vob',u'.swf',u'.mov']
    if ors in baseimgfile or ors in basevideofile:
        return True
    return False