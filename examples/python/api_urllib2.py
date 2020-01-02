#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" 使用urllib2调用API接口

运行环境要求 python2.6/2.7
"""

import urllib2

# api链接
api_url = "https://svip.kdlapi.com/api/getproxy/?orderid=947449222924633&num=100&signature=atvb6a4981d03pvpqalolea9e0k2pmi6&protocol=1&method=2&an_an=1&an_ha=1&format=json&sep=1"

req = urllib2.Request(api_url)
r = urllib2.urlopen(req)

print r.code  # 获取Reponse的返回码
print r.read()  # 获取API返回内容

