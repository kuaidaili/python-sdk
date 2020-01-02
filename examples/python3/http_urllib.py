#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib.request
from urllib.parse import urlencode
import zlib
import ssl
import json
import random

ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消证书验证，避免访问https网页报错

"""使用urllib.request模块请求代理服务器，http和https网页均适用"""

# 要访问的目标网页
page_url = "http://dev.kdlapi.com/testproxy/"
#  api接口，返回格式为json
api_url = "http://kps.kdlapi.com/api/getkps/?orderid=967449798518947&num=2&pt=1&format=json&sep=1"

#  api接口返回的ip
response = urllib.request.urlopen(api_url)
json_dict = json.loads(response.read().decode('utf-8'))
ip_list = json_dict['data']['proxy_list']

# 用户名和密码(私密代理/独享代理)
username = "treezeng"
password = "nrfrqd5o"

# 私密代理或独享代理设置方式
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(ip_list)},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(ip_list)}
}
# 开放代理设置方式
# proxies = {
#     "http": "http://%(proxy)s/" % {'proxy': random.choice(ip_list)},
#     "https": "http://%(proxy)s/" % {'proxy': random.choice(ip_list)}
# }
headers = {
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
}

proxy_handler = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_handler)

# req = urllib.request.Request(url=page_url, headers=headers)
# 发送post请求
data = bytes(urlencode({"info": "send post request"}), encoding='utf-8')
req = urllib.request.Request(url="http://dev.kdlapi.com/testproxy", headers=headers, data=data, method="post")


result = opener.open(req)
print(result.status)  # 获取Response的返回码

content_encoding = result.headers.get('Content-Encoding')
print(content_encoding)
try:
    if "gzip" in content_encoding:
        print(zlib.decompress(result.read(), 16 + zlib.MAX_WBITS).decode('utf-8'))  # 获取页面内容
    else:
        print(result.read().decode('utf-8'))  # 获取页面内容
except TypeError as reason:
    print(reason)
