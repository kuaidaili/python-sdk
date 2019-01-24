# -*- coding: utf-8 -*-
'''
使用selenium下的无窗口浏览器phantomjs的sock5白名单免登录示例
因为是无窗口浏览器，打印了访问网址的title和源代码
'''
from selenium import webdriver

#要访问的目标网页
page_url = "http://dev.kuaidaili.com/testproxy"

#代理服务器ip和端口
proxy = '59.38.241.25:23916'

#代理参数设置
service_args = [
    '--proxy=%s' % proxy,
    '--proxy-type=socks5',
]

#启动PhantomJS并打开网页
driver = webdriver.PhantomJS(service_args = service_args)
driver.get(page_url)

#打出网页title和网页源代码
print driver.title
print driver.page_source

#退出PhantomJS
driver.quit()
