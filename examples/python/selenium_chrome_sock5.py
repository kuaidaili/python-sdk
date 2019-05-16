# _*_ coding:utf‐8 _*
'''
基于selenium下Chrome的sock5白名单访问代理
ubuntu14.04环境
使用虚拟显示实现无窗口Chrome浏览器
官方目前没有支持账号密码认证代理
'''
from xvfbwrapper import Xvfb
from selenium import webdriver

#要访问的目标网页
page_url = "http://dev.kuaidaili.com/testproxy"

#代理服务器ip和端口
proxy = '59.38.241.25:23916'

#复制一份配置文件
desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
#改变配置文件的复制版本.
PROXY = "socks5://" + proxy
desired_capabilities['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "noProxy": None,
    "proxyType": "MANUAL",
    "class": "org.openqa.selenium.Proxy",
    "autodetect": False
}

# 使用新实例驱动
options = webdriver.ChromeOptions()

#如果当前的Chrome支持无窗口，启动无窗口模式
options.add_argument('headless')

#无窗口启动配置好的Chrome
xvfb = Xvfb()
xvfb.start()
driver = webdriver.Chrome(chrome_options=options,desired_capabilities=desired_capabilities)

#尝试访问登陆页面，登录页面有你的代理IP
driver.get(page_url)

#打出网页title和网页源代码
print driver.title
print driver.page_source

#关闭
driver.quit()
xvfb.stop()