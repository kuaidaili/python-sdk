#- * -coding: utf - 8 - * -
#私密代理、独享代理加入白名单之后可以这样使用http/https代理
#加入白名单之后就可以免登录直接使用
#这个是加入白名单后使用http代理的demo
#这个是Windows下的使用无头chrome的示例
from selenium import webdriver

#要访问的目标网页
page_url = "http://dev.kuaidaili.com/testproxy"

#代理服务器ip和端口
proxy = '59.38.241.25:23916'


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--headless')  
chromeOptions.add_argument('--proxy-server=http://' + proxy)  
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get(page_url)

print driver.title
print driver.page_source