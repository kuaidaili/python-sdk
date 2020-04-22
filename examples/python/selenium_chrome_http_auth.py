# -*- coding: utf-8 -*-
"""selenium + chrome + windows + 用户名密码认证
    支持使用http、https、socks代理，支持访问http和https的网页
    如果使用的是socks代理，请在background_js修改scheme: "http"为scheme: "socks"
"""
import os
import zipfile
import requests
import random
import time
from selenium import webdriver


# 目标网页
page_url = "http://dev.kuaidaili.com/testproxy"
# api链接
api_url = "https://dps.kdlapi.com/api/getdps/?orderid=927441114016541&num=10&pt=2&format=json&sep=1"
proxy_ip = requests.get(api_url).json()['data']['proxy_list']

PROXY_HOST, PROXY_PORT = random.choice(proxy_ip).split(":")
PROXY_USER = 'treezeng'  # username
PROXY_PASS = 'nrfrqd5o'  # password

# 动态生成chrome代理插件代码，再使用zipfile模块打包，最后使用chrome_options.add_extension加载插件

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "socks5", /*如果使用的是http/https代理，这个值改为"http"即可*/
        //    scheme: "http", /*如果使用的是socks代理，这个值改为"socks5"即可*/
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    # path = os.path.dirname(os.path.abspath(__file__)) # 如果没有把chromedriver放到python\script\下，则需要指定路径
    chrome_options = webdriver.ChromeOptions()
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(
        # os.path.join(path, 'chromedriver'),
        chrome_options=chrome_options)
    return driver


def main():
    driver = get_chromedriver(use_proxy=True)
    driver.get(page_url)
    time.sleep(5)  # 等待5秒，否则程序执行完毕会立即关闭


if __name__ == '__main__':
    main()
