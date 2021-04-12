#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用requests请求代理服务器
请求http和https网页均适用
"""

import httpx

# 隧道域名:端口号
tunnel = "tpsXXX.kdlapi.com:15818"

# 用户名和密码方式
username = "username"
password = "password"

proxy_url = "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}

proxies = httpx.Proxy(
    url=proxy_url,
    mode="DEFAULT"
)

with httpx.Client(proxies=proxies) as client:
    r = client.get('http://dev.kdlapi.com/testproxy')
    print(r.text)