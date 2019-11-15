# -*- coding: utf-8 -*-
import logging

import requests
import json

orderid = '955793039758159'
api_url = "https://dps.kdlapi.com/api/getdps/?orderid={}&num=1&pt=1&format=json&sep=1"

logger = logging.getLogger(__name__)

def fetch_one_proxy():
    fetch_url = api_url.format(orderid)
    r = requests.get(fetch_url)
    if r.status_code != 200:
        logger.error("fail to fetch proxy")
        return False
    content = json.loads(r.content.decode('utf-8'))
    ips = content['data']['proxy_list']
    return ips[0]

if __name__ == '__main__':
    print("proxy: ", fetch_one_proxy())
