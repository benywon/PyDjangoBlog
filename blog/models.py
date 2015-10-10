# -*- coding: utf-8 -*-
from StringIO import StringIO
import datetime
import os
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models

# Create your models here.
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
from django.contrib import admin
from django.utils import timezone


class BlogsPost(models.Model):
    title = models.CharField(max_length = 150,default='')
    category = models.CharField(max_length = 150,default='其他')
    abstract = models.CharField(max_length = 250,default='暂无简要介绍')
    auther=models.CharField(max_length = 150,default='王炳宁')
    body = UEditorField("描述",width=1300,height=700,max_length=10000,toolbars="full",imagePath="./FileDir/blogmaterials/uploadpic/",filePath="./FileDir/blogmaterials/uploadFile/",blank=True)
    timestamp = models.DateTimeField()
    lastmodified=models.DateTimeField(default=datetime.datetime.now())

class BlogComments(models.Model):
    '每个博客的评论 外键是某个博客'
    Article=models.ForeignKey(BlogsPost)
    auther=models.CharField(max_length = 150,default='匿名')
    body = UEditorField("",width=500,height=300,max_length=10000,toolbars="mini",imagePath="./FileDir/blogmaterials/uploadpic/",filePath="./FileDir/blogmaterials/uploadFile/",blank=True)
    timestamp = models.DateTimeField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

class BlogPoem(models.Model):
    title=models.CharField(max_length = 150)#词牌名
    nav=models.CharField(max_length = 250)#点缀
    body = models.TextField()#词
    auther=models.CharField(max_length = 50,default='王炳宁')#作者
    timestamp = models.DateTimeField()#日期
    isprevious=models.BooleanField(default=False)
class BlogsBlog(models.Model):
    title = models.CharField(max_length = 150)
    authers = models.CharField(max_length = 150,default='王炳宁')
    body = models.TextField()
    timestamp = models.DateTimeField()

class GodTweet(models.Model):
    tweet = models.CharField(max_length=250)
    pos = models.CharField(max_length=50)
    username=models.CharField(max_length=50,default='god')
    timestamp = models.DateTimeField()

class BlogPic(models.Model):
    title=models.CharField(max_length=250)
    headImg = models.ImageField(upload_to = './FileDir/Image/')
    thumb = models.ImageField(upload_to = './FileDir/Thumb/',default='')
    timestamp = models.DateTimeField()
    username=models.CharField(max_length=50,default='god')
    isshow=models.BooleanField(default=False)
    def __str__(self):
        return "%s"%self.title

    def __unicode__(self):
        return self.title
    def save(self, force_update=False, force_insert=False, thumb_size=(300,430)):

        image = Image.open(self.headImg)

        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')
        height=800
        width=800.0/self.headImg.height*self.headImg.width
        image.thumbnail((height,width), Image.ANTIALIAS)

        # save the thumbnail to memory
        temp_handle = StringIO()
        image.save(temp_handle, 'png')
        temp_handle.seek(0) # rewind the file

        # save to the thumbnail field
        suf = SimpleUploadedFile(os.path.split(self.headImg.name)[-1],
                                 temp_handle.read(),
                                 content_type='image/png')
        self.thumb.save(suf.name+'thumb.png', suf, save=False)

        # save the image object
        super(BlogPic, self).save()



class BlogFile(models.Model):
    headFile = models.FileField(upload_to = './FileDir/File/')
    timestamp = models.DateTimeField()

class BlogComment(models.Model):
    comments=models.TextField()
    name=models.CharField(max_length=150)
    canshow=models.BooleanField(default=False)
    timestamp = models.DateTimeField()
class BackUpInfo(models.Model):
    filename=models.CharField(max_length=150)
    timestamp = models.DateTimeField()#日期
class UserLogInfo(models.Model):
    Ip=models.CharField(max_length=150)
    User=models.CharField(max_length=150)
    timestamp = models.DateTimeField()#日期
class GodUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,default='none@none.com')
    timestamp = models.DateTimeField(default=timezone.now)#日期
class UserPosition(models.Model):
    username = models.CharField(max_length=150,default='god')
    Ip=models.IPAddressField(default='127.0.0.1')
    latitude=models.FloatField(default='0.0')
    longtitude=models.FloatField(default='0.0')
    position=models.CharField(max_length=150)
    timestamp = models.DateTimeField(default=timezone.now)#日期