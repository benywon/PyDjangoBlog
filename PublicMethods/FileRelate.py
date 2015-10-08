# -*- coding: utf-8 -*-
import os

__author__ = 'benywon'



def GetFileList(dir, fileList):
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList