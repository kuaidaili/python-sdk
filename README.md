# 快代理API SDK - Python
通过 SDK 可快速调用 API 接口，[查看详情](https://github.com/kuaidaili/python-sdk/tree/master/api-sdk)

# 快代理官方代码样例 - Python

## 调用 API
* 调用 API
    * [urllib2](./examples/api/api_urllib2.py)
    * [urllib](./examples/api/api_urllib.py)
    * [requests](./examples/api/api_requests.py)

## HTTP 代理
* Python2
    * [urllib2](./examples/http_proxy/py2_urllib2.py)
    * [requests](./examples/http_proxy/py2_requests.py)
* Python3
    * [urllib](./examples/http_proxy/py3_urllib.py)
    * [requests](./examples/http_proxy/py3_requests.py)
    * [aiohttp](./examples/http_proxy/py3_aiohttp.py)
    * [httpx](./examples/http_proxy/py3_httpx.py)
    * [websocket 长连接](./examples/http_proxy/py3_websocket.py)
    * [websocket 短连接](./examples/http_proxy/py3_websocket_short.py)
    * [scrapy](./examples/http_proxy/py3_scrapy)
    * [feapder](./examples/http_proxy/py3_feapder.py)
    * [pyppeteer](./examples/http_proxy/py3_pyppeteer.py)
* Selenium
    * [selenium_chrome    白名单验证](./examples/http_proxy/selenium_chrome_whitelist.py)
    * [selenium_chrome    用户名密码验证](./examples/http_proxy/selenium_chrome_username_password.py)
    * [selenium_firefox   白名单验证](./examples/http_proxy/selenium_firefox_whitelist.py)
    * [selenium_firefox   用户名密码验证](./examples/http_proxy/selenium_firefox_username_password.py)
    * [selenium_phantomjs 用户名密码验证](./examples/http_proxy/phantomjs_demo.py)
* ProxyPool
    * [ProxyPool](./examples/http_proxy/proxy_pool.py)

## HTTP 隧道

* Python2
    * [urllib2](./examples/http_proxy_tunnel/py2_urllib2.py)
    * [requests](./examples/http_proxy_tunnel/py2_requests.py)
* Python3
    * [urllib](./examples/http_proxy_tunnel/py3_urllib.py)
    * [requests](./examples/http_proxy_tunnel/py3_requests.py)
    * [aiohttp](./examples/http_proxy_tunnel/py3_aiohttp.py)
    * [httpx](./examples/http_proxy_tunnel/py3_httpx.py)
    * [socket](./examples/http_proxy_tunnel/py3_socket.py)
    * [scrapy](./examples/http_proxy_tunnel/py3_scrapy)
    * [feapder](./examples/http_proxy_tunnel/py3_feapder.py)
    * [pyppeteer](./examples/http_proxy_tunnel/py3_pyppeteer.py)
* Selenium
    * [selenium_chrome  白名单验证](./examples/http_proxy_tunnel/selenium_chrome_whitelist.py)
    * [selenium_chrome  用户名密码验证](./examples/http_proxy_tunnel/selenium_chrome_username_password.py)
    * [selenium_firefox 白名单验证](./examples/http_proxy_tunnel/selenium_firefox_whitelist.py)
    * [selenium_firefox 用户名密码验证](./examples/http_proxy_tunnel/selenium_firefox_username_password.py)

## Socks
* Python2
    * [requests](./examples/socks_proxy/py2_requests.py)
* Python3
    * [requests](./examples/socks_proxy/py3_requests.py)
* Selenium
    * [selenium_chrome 白名单验证](./examples/socks_proxy/selenium_chrome_whitelist.py)
    * [selenium_phantomjs 用户名密码验证](./examples/socks_proxy/phantomjs_demo.py)


# 技术支持

如果您发现代码有任何问题, 请提交 `Issue`。

欢迎提交 `Pull request` 以使代码样例更加完善。

获取更多关于调用 API 和代理服务器使用的资料，请参考[开发者指南](https://help.kuaidaili.com/dev/api/)。

* 技术支持微信：<a href="https://img.kuaidaili.com/img/service_wx.jpg">kuaidaili</a>
* 技术支持QQ：<a href="http://q.url.cn/CDksXo?_type=wpa&qidian=true">800849628</a>
