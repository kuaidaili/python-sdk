# -*- coding: utf-8 -*-
import scrapy


class MainSpider(scrapy.Spider):
    name = "main"
    # allowed_domains = ["ikebo.cn"]
    allowed_domains = ["dev.kdlapi.com"]
    # start_urls = ["https://ikebo.cn"]
    start_urls = ['https://dev.kdlapi.com/testproxy/']
    # start_urls = ['https://dev.kdlapi.com/testproxy/']

    def parse(self, response):
        print('------ response ------', response.text)
