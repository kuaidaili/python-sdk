# -*- coding: utf-8 -*-
'''
使用selenium下的无窗口浏览器phantomjs的shttp白名单免登录示例
因为是无窗口浏览器，所以截了一张图片放在本程序当前目录下
同时打印了访问网址的title和源代码
'''
from selenium import webdriver

#要访问的目标网页
page_url = "http://dev.kuaidaili.com/testproxy"

#代理服务器ip和端口
proxy = '59.38.241.25:23916'

#代理设置参数
service_args = [
    '--proxy=%s' % proxy,
    '--proxy-type=http',
]

#启动PhantomJS，访问网址并截取一张图片
driver = webdriver.PhantomJS(service_args = service_args)
driver.get(page_url)

#打出网页title和网页源代码
print driver.title
print driver.page_source

#退出PhantomJS
driver.quit()
