[调用API](#调用api)
    - [python/api_urllib2.py](#pythonapi_urllib2py)
    - [python/api_urllib.py](#pythonapi_urllibpy)
    - [python/api_requests.py](#pythonapi_requestspy)
[Http代理-Python2部分:](#http代理-python2部分)
    - [python/proxy_urllib2.py](#pythonproxy_urllib2py)
    - [python/proxy_requests.py](#pythonproxy_requestspy)
    - [python/selenium_chrome_http.py](#pythonselenium_chrome_httppy)
    - [python/selenium_phantomjs_http.py](#pythonselenium_phantomjs_httppy)
    - [python/selenium_phantomjs_http_auth.py](#pythonselenium_phantomjs_http_authpy)
[Http代理-Python3部分:](#http代理-python3部分)
    - [python3/http_urllib.py](#python3http_urllibpy)        
    - [python3/http_requests.py](#python3http_requestspy)    
[Http代理-Scrapy部分:](#http代理-scrapy部分)        
    - [scrapy/scrapy_proxy/scrapy_proxy/middlewares.py](#scrapyscrapy_proxyscrapy_proxymiddlewarespy)        - [scrapy/scrapy_proxy/scrapy_proxy/settings.py](#scrapyscrapy_proxyscrapy_proxysettingspy)        
    - [scrapy/scrapy_proxy/scrapy_proxy/spiders/main.py](#scrapyscrapy_proxyscrapy_proxyspidersmainpy)    
[Socks代理-Python2部分:](#socks代理-python2部分)        
    - [python/socks_requests.py](#pythonsocks_requestspy)        
    - [python/socks_urllib2.py](#pythonsocks_urllib2py)        
    - [python/selenium_chrome_sock5.py](#pythonselenium_chrome_sock5py)        
    - [python/selenium_phantomjs_sock5.py](#pythonselenium_phantomjs_sock5py)        
    - [python/selenium_phantomjs_sock5_auth.py](#pythonselenium_phantomjs_sock5_authpy)    
[Socks代理-Python3部分:](#socks代理-python3部分)        
    - [python3/proxy_requests_socks.py](#python3proxy_requests_sockspy)        
    - [python3/proxy_urllib.py](#python3proxy_urllibpy)    
[技术支持](#技术支持)

# 快代理SDK - Python

## 调用API

### python/api_urllib2.py
使用urllib2调用api示例
```
使用提示: 运行环境要求 python2.6/2.7
```

### python/api_urllib.py
使用urllib调用api示例
```
使用提示: 运行环境要求 python3.x
```

### python/api_requests.py
使用requests库调用api示例
```
使用提示:
    * 此样例支持 python 2.6—2.7以及3.3—3.7
    * requests不是python原生库，需要安装才能使用: pip install requests
```

## Http代理-Python2部分:

### python/proxy_urllib2.py
使用urllib2请求Http代理服务器, 支持访问http和https网页, 推荐使用
```
使用提示: 运行环境要求 python2.6/2.7
```

### python/proxy_requests.py
使用requests请求Http代理如武器, 支持使用白名单访问http和https网页, 使用用户名密码不支持访问https网页
```
使用提示: requests不是python原生库, 需要安装才能使用: pip install requests
```

### python/selenium_chrome_http.py
以`白名单`认证形式使用selenium库和Chrome驱动请求Http代理服务器
```
使用提示:
    * 基于白名单的http/https代理Chrome
    * 运行环境要求`python2.x + selenium + Chrome + Chromedriver + xvfb`
    * 安装xvfb：`pip install xvfbwrapper`
    * Ubuntu下开发环境配置参考: https://christopher.su/2015/selenium-chromedriver-ubuntu/
```

### python/selenium_phantomjs_http.py
以`白名单`认证形式使用selenium库和PhantomJS驱动请求Http代理服务器
```
使用提示:
    * 基于白名单的http/https代理PhantomJS
    * 运行环境要求`python2.x + selenium + PhantomJS`
    * `selenium + PhantomJS` 可以直接使用pip安装
```

### python/selenium_phantomjs_http_auth.py
以`用户名密码`认证形式使用selenium库和PhantomJS驱动请求Http代理服务器
```
使用提示:
    * 基于密码认证的http/https代理PhantomJS
    * 运行环境要求`python2.x + selenium + PhantomJS`
    * `selenium + PhantomJS` 可以直接使用pip安装
```

## Http代理-Python3部分:

### python3/http_urllib.py
使用`urllib`库请求Http代理服务器, 支持访问http和https网页
```
使用提示:
    * 基于urllib的代码样例同时支持访问http和https网页，推荐使用
    * 运行环境要求 python3.x
```

### python3/http_requests.py
使用`requests`库请求Http代理服务器, 支持使用白名单访问http,https网页, 使用用户名密码不支持访问https网页
```
使用提示:
    * 基于requests的代码样例支持使用白名单访问http,https网页，使用用户名密码不支持访问https网页
    * requests不是python原生库，需要安装才能使用: pip install requests
```

## Http代理-Scrapy部分:

### scrapy/scrapy_proxy/scrapy_proxy/middlewares.py
设置代理

### scrapy/scrapy_proxy/scrapy_proxy/settings.py
使代理生效

### scrapy/scrapy_proxy/scrapy_proxy/spiders/main.py
使用代理
```
使用提示:
    * http/https网页均可适用
    * scrapy不是python原生库，需要安装才能使用: pip install scrapy
    * 在第一级scrapy_proxy目录下运行如下命令查看结果：scrapy crawl main
```

## Socks代理-Python2部分:

### python/socks_requests.py
使用`requests`库请求Socks代理服务器
```
使用提示:
    * http/https网页均可适用
    * 运行环境要求： requests >= 2.10.0
    * socks支持是`requests`的额外特性，需要安装才能使用: pip install requests[socks]
```

### python/socks_urllib2.py
使用`urllib2`库请求Socks代理服务器
```
使用提示:
    * 运行环境要求 python2.6 / 2.7
    * http/https网页均可适用
    * 使用此样例需要安装PySocks：pip install PySocks
```

### python/selenium_chrome_sock5.py
以`白名单`认证形式使用selenium库和Chrome驱动请求Socks代理服务器
```
使用提示:
    * 运行环境要求 python2.x + selenium + chrome + chrome driver + xvfb
    * socks5代理网页均可适用
    * 安装xvfb：pip install xvfbwrapper
    * 开发环境配置参考: https://christopher.su/2015/selenium-chromedriver-ubuntu/
```

### python/selenium_phantomjs_sock5.py
以`白名单`认证形式使用selenium库和PhantomJS驱动请求Socks代理服务器
```
使用提示:
    * 运行环境要求: python2.x
    * socks5代理网页均可适用
    * 使用此样例需要安装 selenium、PhantomJS
    * PhantomJS 可以直接使用pip安装
```

### python/selenium_phantomjs_sock5_auth.py
以`用户名密码`认证形式使用selenium库和PhantomJS驱动请求Socks代理服务器
```
使用提示:
    * 运行环境要求 python2.x
    * socks5代理http/https网页均可适用
    * 使用此样例需要安装 selenium、PhantomJS
    * PhantomJS 可以直接使用pip安装
```

## Socks代理-Python3部分:

### python3/proxy_requests_socks.py
使用`requests`库请求Socks代理服务器, http/https网页均适用
```
使用提示:
    * http/https网页均可适用
    * 运行环境要求：requests >= 2.10.0
    * socks支持是requests的额外特性，需要安装才能使用: pip install requests[socks]
```

### python3/proxy_urllib.py
使用`urllib`库请求Socks代理服务器, http/https网页均适用
```
使用提示:
    * http/https网页均可适用
    * 请先安装socks: pip install pysocks
```


## 技术支持

如果您发现代码有任何问题, 请提交`Issue`。

欢迎提交`Pull request`以使代码样例更加完善。

获取更多关于调用API和代理服务器使用的资料，请参考[开发者指南](https://help.kuaidaili.com/dev/api/)。

* 技术支持微信：<a href="https://img.kuaidaili.com/img/service_wx.jpg">kuaidaili</a>
* 技术支持QQ：<a href="http://q.url.cn/CDksXo?_type=wpa&qidian=true">800849628</a>
