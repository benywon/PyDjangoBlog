# -*- coding: utf-8 -*-
from django.conf.urls import  url
from blog.adminrelate import TweetPost,poempost,PicPost,FilePost,CommentPost,GodUserLog,LocationPost
from blog.adminrelate.GodUserLog import DataRestore

__author__ = 'benywon'


urlpatterns = [
                       url(r'^Tweet/$',TweetPost.Tweet,name = 'tweets'),
                       url(r'^Tweet/edit/',TweetPost.EditTweet,name = 'tweetsedit'),
                       url(r'^Poem/$',poempost.Poem,name = 'poems'),
                       url(r'^Pic/$',PicPost.Pic,name = 'pic'),
                       url(r'^Location/',LocationPost.Location,name = 'postion'),
                       url(r'^Pic/edit/',PicPost.EditPic,name = 'Picedit'),
                       url(r'^File/$',FilePost.FILE,name = 'file'),
                       url(r'^File/edit/',FilePost.EditFiles,name = 'fileedit'),
                       url(r'^UserLog/',GodUserLog.ShowUserLog,name = 'fileedit'),
                       url(r'^Poem/edit/',poempost.EditPoem,name = 'poemsedit'),
                       url(r'^User/edit/',GodUserLog.EditUser,name = 'poemsedit'),
                       url(r'^Comments/edit/',CommentPost.EditComments,name = 'comment'),
                       url(r'^BackUpFiles/edit/',FilePost.BackUpSee,name = 'backup'),
                       url(r'^ReStore/$',DataRestore,name = 'poemsedit'),
                      ]