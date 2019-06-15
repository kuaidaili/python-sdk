# -*- coding: utf-8 -*-
import base64

import scrapy
from scrapy import Request


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["www.jd.com"]
    start_urls = ["https://www.jd.com"]
    #
    # username = "k_1043"
    # password = "3k0xg183"
    # auth = "Basic %s" % base64.b64encode(('%s:%s' % (username, password)).encode())
    #
    # def start_requests(self):
    #     username = "k_1043"
    #     password = "3k0xg183"
    #     auth = "Basic %s" % base64.b64encode(('%s:%s' % (username, password)).encode())
    #     for url in self.start_urls:
    #         yield Request(url, headers={"User-Agent": "Chrome"})

    # def make_requests_from_url(self, url):
    #     return scrapy.Request(url=url, meta={'download_timeout':3}, callback=self.parse)

    def parse(self, response):
        print('------ response ------', response.text[:300])
