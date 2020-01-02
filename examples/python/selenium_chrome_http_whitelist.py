# _*_ coding:utf‐8 _*
"""
selenium + chrome 使用白名单或开放代理。Windows和Linux都可用
支持http、https、socks
说明：
    1.需要安装google chrome浏览器、chromedriver驱动（下载好，放到python下的Scripts目录下）
    2.需要安装的python包：selenium、requests
    3.Linux下建议使用普通用户运行，因为chrome浏览器默认是不能以root用户运行的。
"""
from selenium import webdriver
import requests
import random

api_url = "http://dps.kdlapi.com/api/getdps/?orderid=927441114016541&num=10&pt=2&format=json&sep=1"
page_url = "https://dev.kdlapi.com/testproxy"  # 要访问的目标网页
proxy_ip = requests.get(api_url).json()['data']['proxy_list']

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % random.choice(proxy_ip))
# 使用socks代理，请启用下面这句
chrome_options.add_argument('--proxy-server=%s' % 'socks5://' + random.choice(proxy_ip))
# chrome_options.add_argument('--headless')  # 无界面启动chrome
chrome = webdriver.Chrome(options=chrome_options)
chrome.get(page_url)
# print(chrome.page_source)
# chrome.quit()