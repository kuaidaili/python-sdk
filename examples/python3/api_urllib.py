#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""使用urllib.request调用API接口(在python3中urllib2被改为urllib.request)
"""

import urllib.request

#api链接
api_url = "http://dev.kdlapi.com/api/getproxy/?orderid=965102959536478&num=100&protocol=1&method=2&an_ha=1&sep=1"

req = urllib.request.urlopen(api_url)

print(req.code)  # 获取Reponse的返回码
print(req.read().decode('utf-8'))  # 获取API返回内容