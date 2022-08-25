#!/usr/bin/env python
# -- coding: utf-8 --

import scrapy

class KdlSpider(scrapy.spiders.Spider):
    name = "kdl"

    def start_requests(self):
        url = "https://dev.kdlapi.com/testproxy"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        print(response.text)


# 如scrapy报ssl异常"('SSL routines', 'ssl3_get_record', 'wrong version number')", 您可以尝试打开以下代码来解决
# from OpenSSL import SSL
# from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory
#
# init = ScrapyClientContextFactory.__init__
# def init2(self, *args, **kwargs):
#     init(self, *args, **kwargs)
#     self.method = SSL.SSLv23_METHOD
# ScrapyClientContextFactory.__init__ = init2
