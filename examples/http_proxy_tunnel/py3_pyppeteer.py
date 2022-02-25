#!/#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
请求http和https网页均适用
"""
import asyncio

from pyppeteer import launch
# 隧道服务器
proxy_raw = "tpsXXX.kdlapi.com:15818"


def accounts():
    # 用户名密码, 若已添加白名单则不需要添加
    username = "username"
    password = "password"
    account = {"username": username, "password": password}
    return account


async def main():
    # 要访问的目标网页
    target_url = "https://dev.kdlapi.com/testproxy"

    browser = await launch({'headless': False, 'args': ['--disable-infobars', '--proxy-server=' + proxy_raw]})
    page = await browser.newPage()

    await page.authenticate(accounts())  # 白名单方式，注释本行（需提前设置白名单）
    await page.setViewport({'width': 1920, 'height': 1080})
    # 使用代理IP发送请求
    await page.goto(target_url)
    await asyncio.sleep(209)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())