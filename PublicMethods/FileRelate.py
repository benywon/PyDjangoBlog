# -*- coding: utf-8 -*-
import os

__author__ = 'benywon'

Myfilekey = 19

def GetFileList(dir, fileList):
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList


def TransferFile(filenme,afterfilename):
    infilecode=get_bytes_from_file(filenme)
    s1 = encrypt(infilecode)
    #将文件打出去
    EncryptedFileName=afterfilename
    with open(EncryptedFileName,'wb') as fileout:
        fileout.write(s1)

def recoverFile(filename):
    data=get_bytes_from_file(filename)
    after=decrypt(data)
    with open(filename.rstrip('_Encry'),'wb') as f:
        f.write(after)


def get_bytes_from_file(filename):
    return open(filename, "rb").read()


def encrypt(s):
    b = bytearray(str(s))
    n = len(b) # 求出 b 的字节数
    c = bytearray(n)
    for i in range(0, n):
        c[i] =255-b[i]
    return c

def decrypt(s):
    c = bytearray(s)
    n = len(c) # 计算 b 的字节数
    b = bytearray(n)
    for i in range(0, n):
        b[i] =255- c[i]
    try:
        return b
    except:
        return "failed"





