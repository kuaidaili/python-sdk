# -*- coding: utf-8 -*-
'''
使用selenium下的无窗口浏览器phantomjs的http认证代理示例
因为是无窗口浏览器，所以截了一张图片放在本程序当前目录下
同时打印了访问网址的title和源代码
'''
from selenium import webdriver
#要访问的目标网页
page_url = "http://dev.kuaidaili.com/testproxy"

#代理服务器的ip和端口
proxy = '59.38.241.25:23916'

#用户名和密码(私密代理/独享代理)
username = 'myusername'
password = 'mypassword'

#代理参数
service_args = [
    '--proxy=%s' % proxy,
    '--proxy-type=http',
    '--proxy-auth=%s:%s' % (username, password)
]

#启动PhantomJS并打开目标网页
driver = webdriver.PhantomJS(service_args=service_args)
driver.get(page_url)

#打印访问网页的title和源代码
print driver.title
print driver.page_source

driver.quit()
