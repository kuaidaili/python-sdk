#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import time

#先下载phantomjs包文件,再填入phantomjs.exe的路径 (路径不要包含中文, 下载地址:https://mirrors.huaweicloud.com/phantomjs/)
executable_path = '${executable_path}'
service_args=[
    '--proxy=host:port', #此处替换您的代理ip,如59.38.241.25:23918
    '--proxy-type=http',
    '--proxy-auth=username:password' #用户名密码
]
driver=webdriver.PhantomJS(service_args=service_args,executable_path=executable_path)
driver.get('https://dev.kdlapi.com/testproxy')

print(driver.page_source)
time.sleep(3)
driver.close()