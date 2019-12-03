# -*- coding: utf-8 -*-
import scrapy


class TestproxySpider(scrapy.Spider):
    name = 'testproxy'
    allowed_domains = ['kdlapi.com']
    start_urls = ['http://dev.kdlapi.com/testproxy']

    def parse(self, response):
        print(response.text)
