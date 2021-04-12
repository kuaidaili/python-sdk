#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用aiohttp请求代理服务器
请求http和https网页均适用

"""

import aiohttp
import asyncio

page_url = "https://dev.kdlapi.com/testproxy"  # 要访问的目标网页

# 隧道域名:端口号
tunnel = "tpsXXX.kdlapi.com:15818"

# 用户名和密码方式
username = "username"
password = "password"

proxy_auth = aiohttp.BasicAuth(username, password)

async def fetch(session, url):
    async with session.get(url, proxy="http://"+tunnel, proxy_auth=proxy_auth) as response:
        return await response.text()

async def main():
    # aiohttp默认使用严格的HTTPS协议检查。可以通过将ssl设置为False来放松认证检查
    # async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, page_url)
        print(html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())