#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  #禁用requests安全建议警告，不影响结果

"""使用requests请求代理服务器，适用于http，https"""

#要访问的目标网页
page_url = "http://dev.kdlapi.com/testproxy/"

#代理服务器
proxy = "59.38.241.25:23916"

#用户名和密码(私密代理/独享代理)
username = "myusername"
password = "mypassword"

proxy_auth = {"http":  "http://%(user)s:%(pwd)s@%(ip)s/" % {'user': username, 'pwd': password, 'ip': proxy},
              "https": "http://%(user)s:%(pwd)s@%(ip)s/" % {'user': username, 'pwd': password, 'ip': proxy}}
proxy_whitelist = {"http":  "http://%(ip)s" % {'ip': proxy},
                   "https": "http://%(ip)s" % {'ip': proxy}}

headers = {"Accept-Encoding": "gzip"}  #使用gzip压缩传输数据让访问更快

############# 白名单设置完成，则无需用户名密码，支持http，https #############
res1 = requests.get(url=page_url, proxies=proxy_whitelist, headers=headers, verify=False)
print(res1.status_code)  #获取Response的返回码
print(res1.content.decode('utf-8'))  #获取页面内容

############# 需要用户名密码来访问代理服务器，支持http，不支持https #############
res2 = requests.get(url=page_url, proxies=proxy_auth, headers=headers)
print(res2.status_code)
print(res2.content.decode('utf-8'))