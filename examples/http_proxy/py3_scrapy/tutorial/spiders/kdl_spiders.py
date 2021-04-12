#!/usr/bin/env python
# -- coding: utf-8 --
import scrapy

class KdlSpider(scrapy.spiders.Spider):
    name = "kdl"

    def start_requests(self):
        url = "https://dev.kdlapi.com/testproxy"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        print(response.status)