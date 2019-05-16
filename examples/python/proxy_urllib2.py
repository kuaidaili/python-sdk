#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""使用urllib2请求代理服务器
请求http和https网页均适用
"""

import urllib2
import base64
import zlib

#要访问的目标网页
page_url = "http://dev.kuaidaili.com/testproxy"

#代理服务器
proxy = "59.38.241.25:23916"

#用户名和密码(私密代理/独享代理)
username = "myusername"
password = "mypassword"


req = urllib2.Request(page_url)
req.add_header("Accept-Encoding", "Gzip") #使用gzip压缩传输数据让访问更快
req.add_header("Proxy-Authorization", "Basic %s" % base64.b64encode('%s:%s' % (username, password)))
req.set_proxy(proxy, "http")
#req.set_proxy(proxy, "https")
r = urllib2.urlopen(req)

print r.code #获取Reponse的返回码
content_encoding = r.headers.getheader("Content-Encoding")
if content_encoding and "gzip" in content_encoding:
    print zlib.decompress(r.read(), 16+zlib.MAX_WBITS) #获取页面内容
else:
    print r.read() #获取页面内容
