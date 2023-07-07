#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
使用requests请求代理服务器
使用Playwright添加IP代理
"""
import requests
from playwright.sync_api import sync_playwright


# 通过API获取代理
def get_proxy(api, params):
    r = requests.get(api, params=params)
    if r.status_code == 200:
        return r.text
    else:
        return None


# 使用Playwright添加私密代理
def playwright_use_proxy(proxy_server):
    if not proxy_server:
        print('获取代理失败')
        return
    with sync_playwright() as p:
        browser = p.chromium.launch(proxy={"server": f'http://{proxy_server}'})
        page = browser.new_page()
        page.goto("https://dev.kdlapi.com/testproxy")
        content = page.content()
        browser.close()
        return content


def main():
    # 定义API配置
    params = {
        'num': 1,
        'pt': 1,
        'sep': 1,
        'secret_id': 'your secret_id',
        'signature': 'yoru signature',
    }
    api = 'https://dps.kdlapi.com/api/getdps/'
    proxy = get_proxy(api, params)
    content = playwright_use_proxy(proxy)
    print(content)


if __name__ == '__main__':
    main()
