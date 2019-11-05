# -*- coding: utf-8 -*-


"""
 @File            :  tps_proxy_urlib.py
 @Software        :  PyCharm
 @description     :  Python3 隧道代理urllib样例
                    请求http和https网页均适用
"""
import urllib.request
import zlib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消证书验证，避免访问https网页报错

#要访问的目标网页
page_urls = ["http://dev.kdlapi.com/testproxy",
             "https://dev.kdlapi.com/testproxy",
             ]

# 隧道服务器
tunnel_host = ""
tunnel_port = ""

# 隧道id和密码
tid = ""
password = ""

proxies = {
    "http": "http://%s:%s@%s:%s/" % (tid, password, tunnel_host, tunnel_port),
    "https": "http://%s:%s@%s:%s/" % (tid, password, tunnel_host, tunnel_port)
}

headers = {
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
}

for url in page_urls:
    proxy_hander = urllib.request.ProxyHandler(proxies)
    opener = urllib.request.build_opener(proxy_hander)

    req = urllib.request.Request(url=url, headers=headers)

    result = opener.open(req)
    print(result.status)  # 获取Response的返回码

    content_encoding = result.headers.get('Content-Encoding')
    if content_encoding and "gzip" in content_encoding:
        print(zlib.decompress(result.read(), 16 + zlib.MAX_WBITS).decode('utf-8'))  # 获取页面内容
    else:
        print(result.read().decode('utf-8'))  # 获取页面内容