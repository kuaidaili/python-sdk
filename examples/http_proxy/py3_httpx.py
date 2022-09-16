#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用requests请求代理服务器
请求http和https网页均适用
"""

import random
import asyncio

import httpx
import requests

page_url = "http://icanhazip.com/"  # 要访问的目标网页

# API接口，返回格式为json
api_url = "http://dps.kdlapi.com/api/getdps/?secret_id=o1fjh1re9o28876h7c08&signature=xxxxx&num=10&pt=1&format=json&sep=1"  # API接口

# API接口返回的proxy_list
proxy_list = requests.get(api_url).json().get('data').get('proxy_list')

# 用户名密码认证(私密代理/独享代理)
username = "username"
password = "password"


async def fetch(url):
    proxies = {
        "http": f"http://{username}:{password}@{random.choice(proxy_list)}",
        "https": f"http://{username}:{password}@{random.choice(proxy_list)}",
    }
    async with httpx.AsyncClient(proxies=proxies, timeout=10) as client:
        resp = await client.get(url)
        print(f"status_code: {resp.status_code}, content: {resp.content}")


def run():
    loop = asyncio.get_event_loop()
    # 异步发出5次请求
    tasks = [fetch(page_url) for _ in range(5)]
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    run()