#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用aiohttp请求代理服务器
请求http和https网页均适用

"""
import random
import asyncio


import aiohttp
import requests

page_url = "http://icanhazip.com/"  # 要访问的目标网页

# API接口，返回格式为json
api_url = "http://dps.kdlapi.com/api/getdps/?orderid=9266892014xxxxx&num=5&pt=1&format=json&sep=1"  # API接口

# API接口返回的proxy_list
proxy_list = requests.get(api_url).json().get('data').get('proxy_list')

# 用户名密码认证(私密代理/独享代理)
username = "username"
password = "password"

proxy_auth = aiohttp.BasicAuth(username, password)


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxy="http://" + random.choice(proxy_list), proxy_auth=proxy_auth) as resp:
            content = await resp.read()
            print(f"status_code: {resp.status}, content: {content}")


def run():
    loop = asyncio.get_event_loop()
    # 异步发出5次请求
    tasks = [fetch(page_url) for _ in range(5)]
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    run()