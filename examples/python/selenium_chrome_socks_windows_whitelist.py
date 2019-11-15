# -*- coding: utf-8 -*-   
"""selenium + chrome + windows + ip白名单
"""
from selenium import webdriver

# 代理服务器
proxy_ip_port = '42.49.11.109:21080'
proxy = 'socks5://' + proxy_ip_port

# 目标网页
page_url = "https://dev.kuaidaili.com/testproxy"

co = webdriver.ChromeOptions()
co.add_argument('--proxy-server=%s' % proxy) # 设置代理
co.add_argument('--headless')  # 无窗口模式, 可选

# 启动chrome
driver = webdriver.Chrome(chrome_options=co)

# 抓取网页
driver.get(page_url)

# 输出网页内容
print(driver.page_source)

# 退出chrome
driver.quit()