# -*- coding: utf-8 -*-


"""
 @File            :  tps_proxy_request.py
 @description     :  Python3 HTTP隧道代理 request样例 使用requests请求代理服务器
                        请求http和https网页均适用
"""

import requests

# 要访问的目标网页
page_urls = ["http://dev.kdlapi.com/testproxy",
             "https://dev.kdlapi.com/testproxy",
             ]

# 隧道服务器
tunnel_host = "tps136.kdlapi.com"
tunnel_port = "15818"

# 隧道用户名密码
tid = "t17465430110330"
password = "nw40z6ni"

proxies = {
        "http": "http://%s:%s@%s:%s/" % (tid, password, tunnel_host, tunnel_port),
        "https": "https://%s:%s@%s:%s/" % (tid, password, tunnel_host, tunnel_port)
    }
headers = {
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
}

for url in page_urls:
    r = requests.get(url, proxies=proxies, headers=headers)
    # 发送post请求
    # r = requests.post("http://dev.kdlapi.com/testproxy", proxies=proxies, data={"info": "send post request"})

    print(r.status_code)  # 获取Reponse的返回码

    if r.status_code == 200:
        r.enconding = "utf-8"  # 设置返回内容的编码
        print(r.content)  # 获取页面内容
