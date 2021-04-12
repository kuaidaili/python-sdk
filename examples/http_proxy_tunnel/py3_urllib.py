#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用urllib请求隧道服务器
请求http和https网页均适用
"""

import urllib.request
import ssl

# 全局取消证书验证，避免访问https网页报错
ssl._create_default_https_context = ssl._create_unverified_context

# 隧道域名:端口号
tunnel = "tpsXXX.kdlapi.com:15818"

# 用户名密码方式
username = "username"
password = "password"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
}

# 白名单方式（需提前设置白名单）
# proxies = {
#     "http": "http://%(proxy)s/" % {"proxy": tunnel},
#     "https": "http://%(proxy)s/" % {"proxy": tunnel}
# }

# 要访问的目标网页
target_url = "https://dev.kdlapi.com/testproxy"

# 使用隧道域名发送请求
proxy_support = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
response = urllib.request.urlopen(target_url)

# 获取页面内容
if response.code == 200:
    print(response.read().decode('utf-8'))