#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""使用urllib2请求socks5代理服务器
请求http和https网页均适用
"""

import urllib2
import base64
import zlib

import socks
from sockshandler import SocksiPyHandler

#要访问的目标网页
page_url = "http://dev.kdlapi.com/testproxy"

#代理服务器
proxy_ip = "59.38.241.25"
proxy_port = 23918

rdns = False #是否在代理服务器上进行dns查询

#用户名和密码(私密代理/独享代理)
username = "myusername"
password = "mypassword"

opener = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, proxy_ip, proxy_port, rdns, username, password))
opener.addheaders = [
    ("Accept-Encoding", "Gzip"), #使用gzip压缩传输数据让访问更快
]
r = opener.open(page_url)

print r.code #获取Reponse的返回码
content = r.read()
content_encoding = r.headers.getheader("Content-Encoding")
if content_encoding and "gzip" in content_encoding:
    print zlib.decompress(content, 16+zlib.MAX_WBITS) #获取页面内容
else:
    print content #获取页面内容