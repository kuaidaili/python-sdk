#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""使用urllib2请求代理服务器
请求http和https网页均适用
"""

import urllib2
import zlib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消证书验证，避免访问https网页报错

#要访问的目标网页
page_url = "http://dev.kdlapi.com/testproxy"

#代理服务器
proxy = "59.38.241.25:23916"

#用户名和密码(私密代理/独享代理)
username = "myusername"
password = "mypassword"

proxies = {
    "http": "http://%(user)s:%(pwd)s@%(ip)s/" % {'user': username, 'pwd': password, 'ip': proxy},
    "https": "http://%(user)s:%(pwd)s@%(ip)s/" % {'user': username, 'pwd': password, 'ip': proxy}
}

req = urllib2.Request(page_url)
req.add_header("Accept-Encoding", "Gzip") #使用gzip压缩传输数据让访问更快
proxy_hander = urllib2.ProxyHandler(proxies)
opener = urllib2.build_opener(proxy_hander)
urllib2.install_opener(opener)
r = urllib2.urlopen(req)

print r.code
content_encoding = r.headers.getheader("Content-Encoding")
if content_encoding and "gzip" in content_encoding:
    print zlib.decompress(r.read(), 16+zlib.MAX_WBITS) #获取页面内容
else:
    print r.read() #获取页面内容
