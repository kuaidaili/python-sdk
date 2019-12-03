#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" 使用urllib2调用API接口

运行环境要求 python2.6/2.7
"""

import urllib2

# api链接
api_url = "开放代理的API链接"

req = urllib2.Request(api_url)
r = urllib2.urlopen(req)

print r.code  # 获取Reponse的返回码
print r.read()  # 获取API返回内容

