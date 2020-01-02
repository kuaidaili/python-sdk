#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""使用urllib2请求代理服务器
请求http和https网页均适用
"""

import urllib2
from urllib import urlencode
import zlib
import ssl
import json
import random

ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消证书验证，避免访问https网页报错

# 要访问的目标网页
page_url = "http://dev.kdlapi.com/testproxy"

# API接口，返回格式为json
api_url = "https://svip.kdlapi.com/api/getproxy/?orderid=947449222924633&num=100&signature=atvb6a4981d03pvpqalolea9e0k2pmi6&protocol=1&method=2&an_an=1&an_ha=1&quality=2&format=json&sep=1"
ip_list = json.loads(urllib2.urlopen(api_url).read(), encoding="utf-8")['data']['proxy_list']
proxy = random.choice(ip_list)

# 用户名和密码(私密代理/独享代理)
username = "username"
password = "password"

# 私密代理、独享代理
# proxies = {
#     "http": "http://%(user)s:%(pwd)s@%(ip)s/" % {'user': username, 'pwd': password, 'ip': proxy},
#     "https": "http://%(user)s:%(pwd)s@%(ip)s/" % {'user': username, 'pwd': password, 'ip': proxy}
# }

# 开放代理
proxies = {
    "http": "http://%(ip)s/" % {'ip': proxy},
    "https": "http://%(ip)s/" % {'ip': proxy}
}
req = urllib2.Request(page_url)
# 发送post请求
# req = urllib2.Request("http://dev.kdlapi.com/testproxy", data=bytes(urlencode({'info': 'send post request'})))
req.add_header("Accept-Encoding", "Gzip") #使用gzip压缩传输数据让访问更快
proxy_hander = urllib2.ProxyHandler(proxies)
opener = urllib2.build_opener(proxy_hander)
urllib2.install_opener(opener)
r = urllib2.urlopen(req)

print r.code
content_encoding = r.headers.getheader("Content-Encoding")
if content_encoding and "gzip" in content_encoding:
    print zlib.decompress(r.read(), 16+zlib.MAX_WBITS) #获取页面内容
else:
    print r.read()  # 获取页面内容
