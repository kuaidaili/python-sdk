# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline


class TestproxySpider(scrapy.Spider):
    name = 'testproxy'
    allowed_domains = ['kdlapi.com']
    start_urls = ['http://dev.kdlapi.com/testproxy']

    # 如果需要发送post请求，需要重写start_requests方法
    # def start_requests(self):
    #     self.url = self.start_urls[0]
    #     yield scrapy.FormRequest(
    #         url=self.url
    #         formdata={"info": "send post request"},
    #         callback=self.parse,
    #         # meta参数可以在不同方法之间传递数据
    #         meta={"key": "value"}
    #     )

    def parse(self, response):
        print(response.text)
        print(response.meta["key"])


if __name__ == "__main__":
    cmdline.execute('scrapy crawl testproxy'.split())