#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
请求http和https网页均适用
"""

import asyncio

import requests
from pyppeteer import launch

# 提取代理API接口，获取1个代理IP
api_url = "http://dps.kdlapi.com/api/getdps/?orderid=9266892014xxxxx&num=1&pt=1&sep=1"
# 获取API接口返回的代理IP
proxy_ip = requests.get(api_url).text
proxy = "http://" + proxy_ip


def accounts():
    # 用户名密码认证(私密代理/独享代理)
    username = "username"
    password = "password"
    account = {"username": username, "password": password}
    return account


async def main():
    # 要访问的目标网页
    target_url = "https://dev.kdlapi.com/testproxy"

    browser = await launch({'headless': False, 'args': ['--disable-infobars', '--proxy-server=' + proxy]})
    page = await browser.newPage()
    await page.authenticate(accounts())  # 白名单方式，注释本行（需提前设置白名单）
    await page.setViewport({'width': 1920, 'height': 1080})
    # 使用代理IP发送请求
    await page.goto(target_url)
    await asyncio.sleep(209)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
