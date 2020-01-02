# _*_ coding:utf‐8 _*

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import random
import re

page_url = "http://dev.kdlapi.com/testproxy"  # 要访问的目标网页
# API接口，返回格式为json
api_url = ""

# API接口返回的ip
proxy = requests.get(api_url).json()['data']['proxy_list']
ip, port = random.choice(proxy).split(":")
port = int(port)

profile = webdriver.FirefoxProfile()
# 不使用代理的协议，注释掉对应的选项即可
settings = {
    'network.proxy.type': 1,  # 0: 不使用代理；1: 手动配置代理
    'network.proxy.http': ip,
    'network.proxy.http_port': port,
    'network.proxy.ssl': ip,  # 如果是https, 需要开启
    'network.proxy.ssl_port': port,
    'network.proxy.socks': ip,
    'network.proxy.socks_port': port,
    # 'network.proxy.ftp': ip,
    # 'network.proxy.ftp_port': port
}
for key, value in settings.items():
    profile.set_preference(key, value)
profile.update_preferences()

options = Options()
# 无界面启动浏览器
options.add_argument('--headless')
driver = webdriver.Firefox(firefox_profile=profile, options=options)
driver.get(page_url)
driver.close()
driver.quit()
