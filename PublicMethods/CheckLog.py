# -*- coding: utf-8 -*- 
__author__ = 'benywon'


def checkLogin(request):
    username=request.COOKIES.get('username')
    if username=='' or username is None:
        return True
    return False