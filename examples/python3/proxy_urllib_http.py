
import urllib.request
import zlib

"""使用urllib.request模块请求代理服务器，http和https网页均适用"""

#import ssl

#ssl._create_default_https_context = ssl._create_unverified_context


#要访问的目标网页
page_url = "https://dev.kdlapi.com/testproxy/"

#代理服务器
proxy = "59.38.241.25:23916"

#用户名和密码(私密代理/独享代理)
username = "myusername"
password = "mypassword"

headers = {"Accept-Encoding": "Gzip"}  #使用gzip压缩传输数据让访问更快

proxy_values = "http://%(user)s:%(pwd)s@%(ip)s" % {'user': username, 'pwd': password, 'ip': proxy}

proxies = {"http": proxy_values, "https": proxy_values, }
print(proxies)
handler = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(handler)

req = urllib.request.Request(url=page_url, headers=headers)

result = opener.open(req)
print(result.status)  #获取Response的返回码

content_encoding = result.headers.get('Content-Encoding')
if content_encoding and "gzip" in content_encoding:
    print(zlib.decompress(result.read(), 16 + zlib.MAX_WBITS).decode('utf-8'))  #获取页面内容
else:
    print(result.read().decode('utf-8'))  #获取页面内容
