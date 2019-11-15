#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" 使用requests调用API接口
	此样例支持Python2.6-2.7以及3.3-3.7
	requests不是python原生库，需要安装才能使用: pip install requests
"""

import requests

#api链接
api_url = "http://dev.kuaidaili.com/api/getproxy/?orderid=965102959536478&num=100&protocol=1&method=2&an_ha=1&sep=1"

r = requests.get(api_url)

print r.status_code #获取Reponse的返回码

if r.status_code == 200:
    r.enconding = "utf-8" #设置返回内容的编码
    print r.content #获取API返回内容

