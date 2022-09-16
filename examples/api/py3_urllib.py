#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""使用urllib.request调用API接口(在python3中urllib2被改为urllib.request)
"""

import urllib.request
import zlib

#api链接
api_url = "http://dev.kdlapi.com/api/getproxy/?secret_id=o1fjh1re9o28876h7c08&signature=xxxxx&num=100&protocol=1&method=2&an_ha=1&sep=1"

headers = {"Accept-Encoding": "Gzip"}  #使用gzip压缩传输数据让访问更快

req = urllib.request.Request(url=api_url, headers=headers)

# 请求api链接
res = urllib.request.urlopen(req)

print(res.code)  # 获取Reponse的返回码
content_encoding = res.headers.get('Content-Encoding')
if content_encoding and "gzip" in content_encoding:
    print(zlib.decompress(res.read(), 16 + zlib.MAX_WBITS).decode('utf-8'))  #获取页面内容
else:
    print(res.read().decode('utf-8'))  #获取页面内容