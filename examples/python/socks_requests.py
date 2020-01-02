#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""使用requests请求socks代理服务器
请求http和https网页均适用
"""

import requests
import random

# 要访问的目标网页
page_url = "http://dev.kdlapi.com/testproxy"

# API接口，返回格式为json
api_url = "https://dps.kdlapi.com/api/getdps/?orderid=927441114016541&num=10&pt=2&format=json&sep=1"
ip_list = requests.get(api_url).json()['data']['proxy_list']
proxy = random.choice(ip_list)

# 用户名和密码(私密代理/独享代理)
username = "treezeng"
password = "nrfrqd5o"

proxies = {
    'http': 'socks5://%s:%s@%s' % (username, password, proxy),
    'https': 'socks5://%s:%s@%s' % (username, password, proxy),
    #提示：如果希望在代理服务器上进行dns解析，把socks5替换成socks5h
}

headers = {
    "Accept-Encoding": "gzip", #使用gzip压缩传输数据让访问更快
}

r = requests.get(page_url, proxies=proxies, headers=headers)
# 发送post请求
# r = requests.post("http://dev.kdlapi.com/testproxy", proxies=proxies, headers=headers, data={'info': "send post request"})

print(r.status_code) #获取Reponse的返回码

if r.status_code == 200:
    r.enconding = "utf-8" #设置返回内容的编码
    print(r.content) #获取页面内容