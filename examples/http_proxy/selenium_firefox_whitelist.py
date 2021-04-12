#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import time

fp = webdriver.FirefoxProfile()
proxy = '${ip:port}'
ip, port = proxy.split(":")
port = int(port)

# 设置代理配置
fp.set_preference('network.proxy.type', 1)
fp.set_preference('network.proxy.http', ip)
fp.set_preference('network.proxy.http_port', port)
fp.set_preference('network.proxy.ssl', ip)
fp.set_preference('network.proxy.ssl_port', port)

driver = webdriver.Firefox(executable_path="${geckodriver_path}", firefox_profile=fp)
driver.get('https://dev.kdlapi.com/testproxy')

# 获取页面内容
print(driver.page_source)

# 延迟3秒后关闭当前窗口，如果是最后一个窗口则退出
time.sleep(3)
driver.close()