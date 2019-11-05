# -*- coding: utf-8 -*-
import scrapy

class MainSpider(scrapy.Spider):
    """
        spider文件, 以爬取京东首页为例
    """
    name = "main"
    allowed_domains = ["www.jd.com"]
    start_urls = ['https://www.jd.com']

    def parse(self, response):
        # 获取返回内容(请求ip)
        print('------ response ------', response.text)