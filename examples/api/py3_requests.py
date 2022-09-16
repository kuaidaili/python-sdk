#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""使用requests请求代理服务器
请求http和https网页均适用
"""

import requests
import random

page_url = "http://dev.kdlapi.com/testproxy"  # 要访问的目标网页
# API接口，返回格式为json
api_url = "http://dps.kdlapi.com/api/getdps?secret_id=o1fjh1re9o28876h7c08&signature=xxxxx&num=10&format=json&sep=1"

# API接口返回的ip
proxy_ip = requests.get(api_url).json()['data']['proxy_list']

# 用户名密码认证(私密代理/独享代理)
username = "username"
password = "password"

proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(proxy_ip)},
    "https": "https://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(proxy_ip)}
}
headers = {
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
}
r = requests.get(page_url, proxies=proxies, headers=headers)
print(r.status_code)  # 获取Response的返回码

if r.status_code == 200:
    r.enconding = "utf-8"  # 设置返回内容的编码
    print(r.content)  # 获取页面内容