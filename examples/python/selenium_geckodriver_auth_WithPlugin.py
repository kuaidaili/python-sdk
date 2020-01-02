# _*_ coding:utf‐8 _*

'''
# Python + Selenium + Firefox 设置密码时，需要使用到两个插件：
# 插件1： modify_headers-0.7.1.1-fx.xpi
# 插件2： closeproxy.xpi
# 这两个插件可以直接在百度上找

# FireFox使用需要用户密码授权的代理，需要用到插件closeproxy.xpi，来自动填写用户名和密码
# 但是，这是这个插件是只支持FireFox 56.0以下的版本。56.0以上的版本，目前没有找到解决方案。
# 建议使用Chrome、Plantomjs等
# 如果非要使用FireFox 56以上的版本的话，可以使用类似pyautogui、win32gui之类的模块，捕获那个输入用户名和密码的窗口，然后进行输入
'''


from selenium import webdriver
from base64 import b64encode
import requests
import random

api_url = "https://dps.kdlapi.com/api/getdps/?orderid=927441114016541&num=10&pt=1&format=json&sep=1"
page_url = "https://dev.kdlapi.com/testproxy"  # 要访问的目标网页
proxy_ip = requests.get(api_url).json()['data']['proxy_list']
host, port = random.choice(proxy_ip).split(":")
proxy = {
    "host": host,
    "port": port,
    "user": "treezeng",
    "pass": "nrfrqd5o"
}

profile = webdriver.FirefoxProfile()

# add new header
profile.add_extension("modify_headers-0.7.1.1-fx.xpi")
profile.set_preference("extensions.modify_headers.currentVersion", "0.7.1.1-fx")
profile.set_preference("modifyheaders.config.active", True)
profile.set_preference("modifyheaders.headers.count", 1)
profile.set_preference("modifyheaders.headers.action0", "Add")
profile.set_preference("modifyheaders.headers.name0", "Proxy-Switch-Ip")
profile.set_preference("modifyheaders.headers.value0", "yes")
profile.set_preference("modifyheaders.headers.enabled0", True)

# add proxy
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', proxy["host"])
profile.set_preference('network.proxy.http_port', int(proxy['port']))
profile.set_preference('network.proxy.ssl', proxy["host"])
profile.set_preference('network.proxy.ssl_port', int(proxy['port']))
profile.set_preference('network.proxy.no_proxies_on', 'localhost, 127.0.0.1')
profile.set_preference("network.proxy.username", proxy['user'])
profile.set_preference("network.proxy.password", proxy['pass'])

# Proxy auto login
profile.add_extension('closeproxy.xpi')
credentials = '{user}:{pass}'.format(**proxy)
credentials = b64encode(credentials.encode('utf-8')).decode('utf-8')
profile.set_preference('extensions.closeproxyauth.authtoken', credentials)

profile.update_preferences()

driver = webdriver.Firefox(profile)
driver.get("https://proxy.mimvp.com/ip.php")
print(driver.page_source)

# driver.quit()