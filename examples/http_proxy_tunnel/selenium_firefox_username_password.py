#!/usr/bin/env python
# encoding: utf-8

import time
from seleniumwire import webdriver # pip install selenium-wire

options = {
    'proxy': {
        'http': 'http://username:password@tpsXXX.kdlapi.com:15818',
        'https': 'http://username:password@tpsXXX.kdlapi.com:15818',
    }
}
driver = webdriver.Firefox(seleniumwire_options=options,executable_path="${geckodriver_path}")

driver.get('https://dev.kdlapi.com/testproxy')

# 获取页面内容
print(driver.page_source)

# 延迟3秒后关闭当前窗口，如果是最后一个窗口则退出
time.sleep(3)
driver.close()