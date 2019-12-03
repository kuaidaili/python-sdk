#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""python2 httplib库使用代理
"""

import httplib
import urllib2
import json
import random
import base64

# 要访问的目标网页
page_url = r"http://dev.kuaidaili.com/testproxy"

# API接口
api_url = "开放代理、独享代理或私密代理的API接口"

# API接口返回的IP
req = urllib2.Request(api_url)
ip_list = json.loads(urllib2.urlopen(api_url).read(), encoding="utf-8")['data']['proxy_list']
ip, port = random.choice(ip_list).split(":")
port = int(port)

# 用户名和密码(私密代理/独享代理)， 如果是开放代理的就不需要用户名和密码
username = "username"
password = "password"

# 用户名和密码需要先进行base64编码，再使用
user_password = "{username}:{password}".format(username=username, password=password)
b64_user_password = "Basic " + base64.b64encode(user_password.encode("utf-8"))

headers = {
    "Proxy-Authorization": b64_user_password,  # 开放代理请注释掉这句
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
# 使用代理
conn = httplib.HTTPConnection(ip, port)
# 发起请求
conn.request("GET", page_url, headers=headers)
response = conn.getresponse()
print response.status
print response.getheaders()
if response.status == 200:
    content = response.read()
    print content


