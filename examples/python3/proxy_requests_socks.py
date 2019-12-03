"""使用requests请求socks代理服务器，需要安装pysocks库：pip install pysocks
请求http和https网页均适用
"""

import requests
import random

# 要访问的目标网页
page_url = "https://dev.kdlapi.com/testproxy"
# API接口，提示：代理类型请勾选socks4/socks5，返回格式勾选json
api_url = ""

# API 接口返回的ip, 返回格式为json
ip_list = requests.get(api_url).json()['data']['proxy_list']

# 用户名和密码(私密代理/独享代理)
username = "username"
password = "password"

proxies = {
    'http': 'socks5://%s:%s@%s' % (username, password, random.choice(ip_list)),
    'https': 'socks5://%s:%s@%s' % (username, password, random.choice(ip_list)),
    # 提示：如果希望在代理服务器上进行dns解析，把socks5替换成socks5h
}

headers = {
    "Accept-Encoding": "gzip",  # 使用gzip压缩传输数据让访问更快
}

r = requests.get(page_url, proxies=proxies, headers=headers)
print(r.status_code)  # 获取Response的返回码

if r.status_code == 200:
    print(r.text)
