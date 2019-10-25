# -*- coding: utf-8 -*-   
"""
 selenium + chrome + windows + 用户名密码认证
"""
from selenium import webdriver

proxyauth_plugin_path = create_proxyauth_extension(
    proxy_host="42.49.11.109",  # 代理服务器ip
    proxy_port=21080,           # 代理服务器端口
    proxy_username="yourusername",    # 用户名
    proxy_password="yourpassword",  # 密码
    scheme='socks5',  # socks5协议
)

# 目标网页
page_url = "https://dev.kuaidaili.com/testproxy"

co = webdriver.ChromeOptions()
co.add_argument("--start-maximized")  # 最大化窗口, 不加可能报错
co.add_extension(proxyauth_plugin_path) # 添加扩展

# 启动chrome, 抓取网页
driver = webdriver.Chrome(chrome_options=co)
driver.get("https://dev.kuaidaili.com/testproxy")

# 输出网页内容
print(driver.page_source)

# 自动生成扩展的函数
def create_proxyauth_extension(proxy_host, proxy_port,
                               proxy_username, proxy_password,
                               scheme='http', plugin_path=None):
    import string
    import zipfile

    if plugin_path is None:
        plugin_path = 'vimm_chrome_proxyauth_plugin.zip'

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",   
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = string.Template(
    """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "${scheme}",
                host: "${host}",
                port: parseInt(${port})
              },
              bypassList: ["foobar.com"]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "${username}",
                password: "${password}"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path