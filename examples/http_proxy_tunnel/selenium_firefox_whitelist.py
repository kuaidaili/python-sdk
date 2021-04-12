#!/usr/bin/env python
# encoding: utf-8

import time
from selenium import webdriver


fp = webdriver.FirefoxProfile()
proxy_ip = "tpsXXX.kdlapi.com"  # 隧道服务器域名
proxy_port = 15818  # 端口号

fp.set_preference('network.proxy.type', 1)
fp.set_preference('network.proxy.http', proxy_ip)
fp.set_preference('network.proxy.http_port', proxy_port)
fp.set_preference('network.proxy.ssl', proxy_ip)
fp.set_preference('network.proxy.ssl_port', proxy_port)

driver = webdriver.Firefox(executable_path="${geckodriver_path}", firefox_profile=fp)
driver.get('https://dev.kdlapi.com/testproxy')

# 获取页面内容
print(driver.page_source)

# 延迟3秒后关闭当前窗口，如果是最后一个窗口则退出
time.sleep(3)
driver.close()