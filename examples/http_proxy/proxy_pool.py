#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import time
import random
import threading

import requests


class ProxyPool():

    def __init__(self, secret_id, secret_token, proxy_count):
        self.secret_id = secret_id
        self.signature = secret_token
        self.proxy_count = proxy_count if proxy_count < 50 else 50 # 池子维护的IP总数，建议一般不要超过50
        self.alive_proxy_list = []  # 活跃IP列表

    def _fetch_proxy_list(self, count):
        """调用快代理API获取代理IP列表"""
        try:
            res = requests.get("http://dps.kdlapi.com/api/getdps/?secret_id=%s&signature=%s&num=%s&pt=1&sep=1&f_et=1&format=json" % (self.secret_id, self.signature, count))
            return [proxy.split(',') for proxy in res.json().get('data').get('proxy_list')]
        except:
            print("API获取IP异常，请检查订单")
        return []

    def _init_proxy(self):
        """初始化IP池"""
        self.alive_proxy_list = self._fetch_proxy_list(self.proxy_count)

    def add_alive_proxy(self, add_count):
        """导入新的IP, 参数为新增IP数"""
        self.alive_proxy_list.extend(self._fetch_proxy_list(add_count))

    def get_proxy(self):
        """从IP池中获取IP"""
        return random.choice(self.alive_proxy_list)[0] if self.alive_proxy_list else ""

    def run(self):
        sleep_seconds = 1
        self._init_proxy()
        while True:
            for proxy in self.alive_proxy_list:
                proxy[1] = float(proxy[1]) - sleep_seconds  # proxy[1]代表此IP的剩余可用时间
                if proxy[1] <= 3:
                    self.alive_proxy_list.remove(proxy)  # IP还剩3s时丢弃此IP
            if len(self.alive_proxy_list) < self.proxy_count:
                self.add_alive_proxy(self.proxy_count - len(self.alive_proxy_list))
            time.sleep(sleep_seconds)

    def start(self):
        """开启子线程更新IP池"""
        t = threading.Thread(target=self.run)
        t.setDaemon(True)  # 将子线程设为守护进程，主线程不会等待子线程结束，主线程结束子线程立刻结束
        t.start()


def parse_url(proxy):
    # 用户名密码认证(私密代理/独享代理)
    username = "username"
    password = "password"
    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,"proxy": proxy},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,"proxy": proxy}
    }

    # 白名单方式（需提前设置白名单）
    # proxies = {
    #     "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
    #     "https": "http://%(proxy)s/" % {"proxy": proxy_ip}
    # }

    # 要访问的目标网页
    target_url = "https://dev.kdlapi.com/testproxy"
    # 使用代理IP发送请求
    response = requests.get(target_url, proxies=proxies)
    # 获取页面内容
    if response.status_code == 200:
        print(response.text)


if __name__ == '__main__':
    proxy_pool = ProxyPool('o1fjh1re9o28876h7c08', 'xxxxxx', 30) # 订单SecretId, 签名(secret_token), 池子中维护的IP数
    proxy_pool.start()
    time.sleep(1)  # 等待IP池初始化

    proxy = proxy_pool.get_proxy() # 从IP池中提取IP
    if proxy:
        parse_url(proxy)