#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

"""使用requests请求代理服务器，适用于http，https"""

#要访问的目标网页
page_url = "http://dev.kdlapi.com/testproxy/"

#代理服务器
proxy = "59.38.241.25:23916"

#用户名和密码(私密代理/独享代理)
username = "myusername"
password = "mypassword"

proxies = {
    "http": "http://%(user)s:%(pwd)s@%(ip)s/" % {'user': username, 'pwd': password, 'ip': proxy},
    "https": "http://%(user)s:%(pwd)s@%(ip)s/" % {'user': username, 'pwd': password, 'ip': proxy}
}

headers = {
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
}

res = requests.get(url=page_url, proxies=proxies, headers=headers)
print(res.status_code) # 获取Reponse的返回码
if res.status_code == 200:
    print(res.content.decode('utf-8')) # 获取页面内容
