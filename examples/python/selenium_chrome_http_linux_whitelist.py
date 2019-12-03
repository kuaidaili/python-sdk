# _*_ coding:utf‐8 _*
"""基于selenium下Chrome的http白名单访问代理
ubuntu14.04环境
目前使用虚拟显示支持无窗口操作
目前不能支持账户密码登录
"""
from selenium import webdriver
# from xvfbwrapper import Xvfb ### fcntl
import requests
import random

# 代理服务器IP和端口
api_url = "https://svip.kdlapi.com/api/getproxy/?orderid=947449222924633&num=100&protocol=1&method=2&an_an=1&an_ha=1&quality=2&format=json&sep=1"
ip_list = requests.get(api_url).json()['data']['proxy_list']
proxy = random.choice(ip_list)
print(proxy)
#要访问的目标网页
page_url = 'http://dev.kuaidaili.com/testproxy'

#配置请求代理参数
PROXY = "http://" + proxy
# 复制一份配置文件
desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
# 改变配置文件的复制版本.
desired_capabilities['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "noProxy": None,
    "proxyType": "MANUAL",
    "class": "org.openqa.selenium.Proxy",
    "autodetect": False
}

#使用新实例驱动
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(firefox_options=options)
driver.get("http://dev.kdlapi.com/testproxy")
# 无窗口启动Chrome
# xvfb = Xvfb()
# xvfb.start()
# driver = webdriver.Chrome(chrome_options=options,desired_capabilities=desired_capabilities)
#
# #尝试访问登陆页面，登录页面有你的代理IP
# driver.get(page_url)
#
# #打印访问网页的title和源代码
# print driver.title
# print driver.page_source
#
# #关闭
# driver.quit()
# xvfb.stop()