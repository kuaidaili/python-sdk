#!/usr/bin/env python
# encoding: utf-8

import time

from seleniumwire import webdriver # pip install selenium-wire

username = 'username' # 请替换您的用户名和密码
password = 'password'
proxy_ip = '59.38.241.25:23916' # 请替换您提取到的代理ip
options = {
    'proxy': {
        'http': "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
        'https': "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
    }
}

driver = webdriver.Firefox(seleniumwire_options=options,executable_path="${geckodriver_path}")

driver.get('https://dev.kdlapi.com/testproxy')

# 获取页面内容
print(driver.page_source)

# 延迟3秒后关闭当前窗口，如果是最后一个窗口则退出
time.sleep(3)
driver.close()