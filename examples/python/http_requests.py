# -*- coding: utf-8 -*-
"""python3提取api链接并使用requests库进行http代理"""
import requests
import random

page_url = "http://dev.kdlapi.com/testproxy"  # 要访问的目标网页
# API接口，返回格式为json
api_url = ""

# API接口返回的ip
proxy_ip = requests.get(api_url).json()['data']['proxy_list']
# 用户名和密码(私密代理/独享代理)
username = ""
password = ""

# 私密代理或独享代理
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(proxy_ip)},
    "https": "https://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(proxy_ip)}
}
# 开放代理
# proxies = {
#     "http": "http://%(proxy)s/" % {'proxy': random.choice(proxy_ip)},
#     "https": "https://%(proxy)s/" % {'proxy': random.choice(proxy_ip)}
# }
headers = {
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
}
r = requests.get(page_url, proxies=proxies, headers=headers)
print(r.status_code)  # 获取Response的返回码

if r.status_code == 200:
    r.enconding = "utf-8"  # 设置返回内容的编码
    print(r.content)  # 获取页面内容