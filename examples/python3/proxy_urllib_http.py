#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import zlib
import json
import random

"""使用urllib.request模块请求代理服务器，http和https网页均适用"""

#import ssl

#ssl._create_default_https_context = ssl._create_unverified_context


# 要访问的目标网页
page_url = "https://dev.kdlapi.com/testproxy/"

# API接口, 返回格式为json
api_url = "https://svip.kdlapi.com/api/getproxy/?orderid=947449222924633&num=100&protocol=1&method=2&an_an=1&an_ha=1&quality=2&format=json&sep=1"
# API接口返回的ip
response = urllib.request.urlopen(api_url)
json_dict = json.loads(response.read().decode('utf-8'))
ip_list = json_dict['data']['proxy_list']

# 用户名和密码(私密代理/独享代理)
username = "username"
password = "password"

headers = {"Accept-Encoding": "Gzip"}  # 使用gzip压缩传输数据让访问更快

#proxy_values = "http://%(user)s:%(pwd)s@%(ip)s" % {'user': username, 'pwd': password, 'ip': random.choice(ip_list)}
# 开放代理不需要密码
proxy_values = "%(ip)s" % {'ip': random.choice(ip_list)}

proxies = {"http": proxy_values, "https": proxy_values}
print(proxies)
handler = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(handler)

req = urllib.request.Request(url=page_url, headers=headers)

result = opener.open(req)
print(result.status)  # 获取Response的返回码

content_encoding = result.headers.get('Content-Encoding')
if content_encoding and "gzip" in content_encoding:
    print(zlib.decompress(result.read(), 16 + zlib.MAX_WBITS).decode('utf-8'))  # 获取页面内容
else:
    print(result.read().decode('utf-8'))  # 获取页面内容
