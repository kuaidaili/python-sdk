# -*- coding: utf-8 -*-


"""隧道代理urllib样例使用urllib2请求代理服务器
    请求http和https网页均适用
"""

import urllib2
from urllib import urlencode
import zlib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消证书验证，避免访问https网页报错

#要访问的目标网页
page_urls = ["http://dev.kdlapi.com/testproxy",
             "https://dev.kdlapi.com/testproxy",
             ]

# 隧道服务器
tunnel_host = "tps136.kdlapi.com"
tunnel_port = "15818"

# 隧道id和密码
tid = "t17465430110330"
password = "nw40z6ni"

proxies = {
    "http": "http://%s:%s@%s:%s/" % (tid, password, tunnel_host, tunnel_port),
    "https": "http://%s:%s@%s:%s/" % (tid, password, tunnel_host, tunnel_port)
}

for url in page_urls:
    req = urllib2.Request(url)
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
        print r.read()  # 获取页面内容

# 发送post请求
# req = urllib2.Request("http://dev.kdlapi.com/testproxy")
# req.add_header("Accept-Encoding", "Gzip")  # 使用gzip压缩传输数据让访问更快
# proxy_hander = urllib2.ProxyHandler(proxies)
# opener = urllib2.build_opener(proxy_hander)
# urllib2.install_opener(opener)
# r = urllib2.urlopen(req, data=bytes(urlencode({"info": "send post request"})))
#
# content_encoding = r.headers.getheader("Content-Encoding")
# if content_encoding and "gzip" in content_encoding:
#     print zlib.decompress(r.read(), 16+zlib.MAX_WBITS) #获取页面内容
# else:
#     print r.read()  # 获取页面内容