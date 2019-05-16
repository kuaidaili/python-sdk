#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""使用requests请求代理服务器
请求http适用网页适用，不适用请求https网页
"""

import requests
import base64

#要访问的目标网页
page_url = "http://dev.kuaidaili.com/testproxy"

#代理服务器
proxy = "59.38.241.25:23916"

#用户名和密码(私密代理/独享代理)
username = "myusername"
password = "mypassword"

proxies = {
    'http': 'http://%s:%s@%s' % (username, password, proxy),
    'https': 'http://%s:%s@%s' % (username, password, proxy),
    #提示：如果希望在代理服务器上进行dns解析，把socks5替换成socks5h
}

headers = {
    "Accept-Encoding": "Gzip", #使用gzip压缩传输数据让访问更快
    "Proxy-Authorization": "Basic %s" % base64.b64encode('%s:%s' % (username, password)), #不需要验证(如开放代理)，就不带这个header 
}

r = requests.get(page_url, proxies=proxies, headers=headers, verify=False)

print r.status_code #获取Reponse的返回码

if r.status_code == 200:
    r.enconding = "utf-8" #设置返回内容的编码
    print r.content #获取页面内容
