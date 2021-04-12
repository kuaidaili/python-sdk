#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用socket请求隧道服务器
请求http和https网页均适用
"""

import socket
import socks  # pip install PySocks

socks.set_default_proxy(socks.HTTP, addr='tpsXXX.kdlapi.com', port=15818, username='username',password='password')  # 设置代理类型为HTPP
# socks.set_default_proxy(socks.SOCKS5, addr='tpsXXX.kdlapi.com', port=20818)  # 设置代理类型为socks
socket.socket = socks.socksocket  # 把代理添加到socket


def main():
    sock = socket.socket()
    sock.connect(('dev.kdlapi.com', 80))  # 连接
    # 按照http协议格式完整构造http request
    request = 'GET https://dev.kdlapi.com/testproxy \r\nUser-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36\r\n Connection: close'  # 包含method, url, headers

    response = b''  # 接收数据
    sock.send(request.encode())  # 发送请求
    chunk = sock.recv(1024)  # 一次接收1024字节数据
    while chunk:  # 循环接收数据，若没有数据了说明已接收完
        response += chunk
        chunk = sock.recv(1024)
    print(response.decode())


if __name__ == '__main__':
    main()