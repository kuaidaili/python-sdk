#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=socks5://${ip:port}')  # 代理IP:端口号
# ${chromedriver_path}: chromedriver驱动存放路径
driver = webdriver.Chrome(executable_path="${chromedriver_path}", chrome_options=chrome_options)
driver.get("https://dev.kdlapi.com/testproxy")

# 获取页面内容
print(driver.page_source)

# 延迟3秒后关闭当前窗口，如果是最后一个窗口则退出
time.sleep(3)
driver.close()