"""使用urllib请求socks5代理服务器
请求http和https网页均适用
"""

import urllib.request
import socks
import zlib
from sockshandler import SocksiPyHandler

# 要访问的目标网页
page_url = "https://dev.kdlapi.com/testproxy"

# 代理服务器
proxy_ip = "59.38.241.25"
proxy_port = 23916

rdns = False  # 是否在代理服务器上进行dns查询

# 用户名和密码(私密代理/独享代理)
username = "myusername"
password = "mypassword"

opener = urllib.request.build_opener(SocksiPyHandler(socks.SOCKS5, proxy_ip, proxy_port, rdns, username, password))
opener.addheaders = [
    ("Accept-Encoding", "Gzip"), #使用gzip压缩传输数据让访问更快
]
r = opener.open(page_url)

print(r.code)  # 获取Reponse的返回码
content = r.read()

content_encoding = r.headers.get_all("Content-Encoding")
if content_encoding and "gzip" in content_encoding:
    print(zlib.decompress(content, 16 + zlib.MAX_WBITS).decode('utf8'))  # 有gzip压缩时获取页面内容
else:
    print(content.decode('utf-8'))  # 无gzip压缩时获取页面内容
