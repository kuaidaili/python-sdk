#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import string
import zipfile
import time


def create_proxyauth_extension(tunnelhost, tunnelport, proxy_username, proxy_password, scheme='http', plugin_path=None):
    """代理认证插件

    args:
        tunnelhost (str): 你的代理地址或者域名（str类型）
        tunnelport (int): 代理端口号（int类型）
        proxy_username (str):用户名（字符串）
        proxy_password (str): 密码 （字符串）
    kwargs:
        scheme (str): 代理方式 默认http
        plugin_path (str): 扩展的绝对路径

    return str -> plugin_path
    """

    if plugin_path is None:
        plugin_path = 'vimm_chrome_proxyauth_plugin.zip'

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

    background_js = string.Template(
        """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "${scheme}",
                    host: "${host}",
                    port: parseInt(${port})
                },
                bypassList: ["foobar.com"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "${username}",
                    password: "${password}"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """
    ).substitute(
        host=tunnelhost,
        port=tunnelport,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    return plugin_path


proxyauth_plugin_path = create_proxyauth_extension(
    tunnelhost="${tunnelhost}",  # 隧道域名
    tunnelport="${tunnelport}",  # 端口号
    proxy_username="${username}",  # 用户名
    proxy_password="${password}"  # 密码
)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension(proxyauth_plugin_path)
# ${chromedriver_path}: chromedriver驱动存放路径
driver = webdriver.Chrome(executable_path="${chromedriver_path}", chrome_options=chrome_options)
driver.get("https://dev.kdlapi.com/testproxy")

# 获取页面内容
print(driver.page_source)

# 延迟3秒后关闭当前窗口，如果是最后一个窗口则退出
time.sleep(3)
driver.close()