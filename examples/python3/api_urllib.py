#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""使用urllib.request调用API接口(在python3中urllib2被改为urllib.request)
"""

import urllib.request

#api链接
api_url = "http://svip.kdlapi.com/api/getproxy/?orderid=947449222924633&num=100&signature=atvb6a4981d03pvpqalolea9e0k2pmi6&protocol=1&method=2&an_an=1&an_ha=1&format=json&sep=1"

req = urllib.request.urlopen(api_url)

print(req.code)  # 获取Reponse的返回码
print(req.read().decode('utf-8'))  # 获取API返回内容