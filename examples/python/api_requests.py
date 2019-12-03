#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 使用requests调用API接口
	此样例支持Python2.6-2.7以及3.3-3.7
	requests不是python原生库，需要安装才能使用: pip install requests
"""

import requests

# API接口
api_url = "开放代理的API链接"

r = requests.get(api_url)

print r.status_code  # 获取Reponse的返回码

if r.status_code == 200:
    r.enconding = "utf-8"  # 设置返回内容的编码
    print r.content  # 获取API返回内容
