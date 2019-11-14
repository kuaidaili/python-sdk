# -*- coding: utf-8 -*-
"""selenium + chrome + windows + ip白名单
"""

from selenium import webdriver

# 代理服务器ip和端口
proxy = '42.49.11.109:16816'

# 目标网页
page_url = "https://dev.kuaidaili.com/testproxy"

co = webdriver.ChromeOptions()
co.add_argumen('--proxy-server=%s' % proxy) # 设置代理
co.add_argument('--headless')  # 无窗口模式, 可选

# 启动chrome
driver = webdriver.Chrome(chrome_options=co)

# 抓取网页
driver.get(page_url)

# 输出网页内容
print(driver.page_source)

# 退出chrome
driver.quit()