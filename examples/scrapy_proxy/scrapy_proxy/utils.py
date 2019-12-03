# -*- coding: utf-8 -*-

import requests
import logging
import random

logger = logging.getLogger(__name__)


def get_one_proxy(api_url):
    """ 使用API接口获取一个代理IP"""
    # API接口
    api_url = api_url
    # API接口返回的IP
    r = requests.get(api_url)
    if r.status_code != 200:
        logger.error("fail to get proxy")
        return None
    ip_list = r.json()['data']['proxy_list']
    return random.choice(ip_list)


if __name__ == '__main__':
    print("proxy: ", get_one_proxy())
