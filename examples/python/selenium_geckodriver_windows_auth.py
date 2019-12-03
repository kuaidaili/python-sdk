# _*_ coding:utf‐8 _*

'''
# Python + Selenium + Firefox 设置密码时，需要使用到两个插件：
# 插件1： modify_headers-0.7.1.1-fx.xpi
# 插件2： closeproxy.xpi
# 这两个插件可以直接在百度上找

# FireFox使用需要用户密码授权的代理，需要用到插件closeproxy.xpi，来自动填写用户名和密码
# 但是，这是这个插件是只支持FireFox 56.0以下的版本。56.0以上的版本，目前没有找到解决方案。
# 建议使用Chrome、Plantomjs等
'''




from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import *
from pyvirtualdisplay import Display
from base64 import b64encode

proxy = {
    "host": "223.214.203.192",
    "port": "23222",
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
profile.set_preference('network.proxy.ssl', proxy["host"])
profile.set_preference('network.proxy.ssl_port', int(proxy['port']))
profile.set_preference('network.proxy.no_proxies_on', 'localhost, 127.0.0.1')
# 如果是https, 需要开启

# profile.set_preference("network.proxy.username", 'aaaaa')
# profile.set_preference("network.proxy.password", 'bbbbb')

# Proxy auto login
profile.add_extension('closeproxy.xpi')
credentials = '{user}:{pass}'.format(**proxy)
credentials = b64encode(credentials.encode('utf-8')).decode('utf-8')
profile.set_preference('extensions.closeproxyauth.authtoken', credentials)

profile.update_preferences()

driver = webdriver.Firefox(profile)
driver.get("https://proxy.mimvp.com/ip.php")
print driver.page_source

# driver.quit()