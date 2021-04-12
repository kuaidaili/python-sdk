#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用urllib请求代理服务器
请求http和https网页均适用
"""

import urllib.request
import ssl

# 全局取消证书验证，避免访问https网页报错
ssl._create_default_https_context = ssl._create_unverified_context

# 提取代理API接口，获取1个代理IP
api_url = "http://dps.kdlapi.com/api/getdps/?orderid=9266892014xxxxx&num=1&pt=1&sep=1"

# 获取API接口返回的IP
proxy_ip = urllib.request.urlopen(api_url).read().decode('utf-8')

# 用户名密码认证(私密代理/独享代理)
username = "username"
password = "password"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
}

# 白名单方式（需提前设置白名单）
# proxies = {
#     "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
#     "https": "http://%(proxy)s/" % {"proxy": proxy_ip}
# }

# 要访问的目标网页
target_url = "https://dev.kdlapi.com/testproxy"

# 使用代理IP发送请求
proxy_support = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
response = urllib.request.urlopen(target_url)

# 获取页面内容
if response.code == 200:
    print(response.read().decode('utf-8'))