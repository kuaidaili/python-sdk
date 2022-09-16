#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""使用urllib2调用API接口
"""

import urllib2
import zlib

#api链接
api_url = "http://dev.kdlapi.com/api/getproxy/?secret_id=o1fjh1re9o28876h7c08&signature=xxxxx&num=100&protocol=1&method=2&an_ha=1&sep=1"

req = urllib2.Request(api_url)
req.add_header("Accept-Encoding", "Gzip") #使用gzip压缩传输数据让访问更快
r = urllib2.urlopen(req)

print r.code #获取Reponse的返回码
content_encoding = r.headers.getheader("Content-Encoding")
if content_encoding and "gzip" in content_encoding:
    print zlib.decompress(r.read(), 16+zlib.MAX_WBITS) #获取页面内容
else:
    print r.read() #获取页面内容