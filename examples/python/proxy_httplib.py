#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""python2 httplib库使用代理
"""

import httplib
import urllib2
import urllib
import json
import random
import base64

# 要访问的目标网页
page_url = r"http://dev.kuaidaili.com/testproxy"

# API接口
api_url = "https://kps.kdlapi.com/api/getkps/?orderid=967449798518947&num=2&pt=1&format=json&sep=1"

# API接口返回的IP
req = urllib2.Request(api_url)
ip_list = json.loads(urllib2.urlopen(api_url).read(), encoding="utf-8")['data']['proxy_list']
ip, port = random.choice(ip_list).split(":")
port = int(port)

# 用户名和密码(私密代理/独享代理)， 如果是开放代理的就不需要用户名和密码
username = "treezeng"
password = "nrfrqd5o"

# 用户名和密码需要先进行base64编码，再使用
user_password = "{username}:{password}".format(username=username, password=password)
b64_user_password = "Basic " + base64.b64encode(user_password.encode("utf-8"))

headers = {
    "Proxy-Authorization": b64_user_password,  # 开放代理请注释掉这句
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
# 使用代理
conn = httplib.HTTPConnection(ip, port)
conn.request("GET", page_url, headers=headers)

# 发起请求
# body = bytes(urllib.urlencode({"info": "send post request"}))
# conn.request("POST", "http://dev.kdlapi.com/testproxy", body=body, headers=headers)

response = conn.getresponse()
print response.status
print response.getheaders()
if response.status == 200:
    content = response.read()
    print content
