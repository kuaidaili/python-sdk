#!/usr/bin/env python
#-*- coding: utf-8 -*-


import httplib

#要访问的目标网页
page_url = "http://dev.kuaidaili.com/testproxy"

#代理服务器
proxy = "59.38.241.25:23916"

#用户名和密码(私密代理/独享代理)
username = "myusername"
password = "mypassword"

headers = {
    "Proxy-Authorization": "Basic a3BzbW9uaXRvcjprZGxtMjAxNg==",
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Connection": "close",
}

conn = httplib.HTTPSConnection(proxy, timeout=5)
conn.request("GET", page_url, headers=headers)
r = conn.getresponse()
print r.status
print r.getheaders()
if r.status == 200:
    content = r.read()
    print content

