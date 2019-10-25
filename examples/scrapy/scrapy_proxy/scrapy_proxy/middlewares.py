# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import logging

import scrapy
from scrapy import signals

# # 代理服务器ip和端口 <开放代理或其他代理已添加白名单>
# proxy = '59.38.241.25:23916'
#
# # 非开放代理且未添加白名单，需用户名密码认证
# username = "myusername"
# password = "mypassword"
# proxy = '%s:%s@%s' % (username, password, proxy)

# 代理服务器ip和端口 <开放代理或其他代理已添加白名单>
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

from .utils import fetch_one_proxy

# 非开放代理且未添加白名单，需用户名密码认证
username = "k_1043"
password = "3k0xg183"
proxy = fetch_one_proxy() # 获取一个代理

THRESHOLD = 2  # 换ip阈值
fail_time = 0  # 此ip异常次数

logger = logging.getLogger(__name__)

# 代理中间件
class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy_url = 'http://%s:%s@%s' % (username, password, proxy)
        request.meta['proxy'] = proxy_url
        logger.debug("using proxy: {}".format(request.meta['proxy']))
        logger.debug("fail_time: {}".format(fail_time))
        auth = "Basic %s" % (base64.b64encode(('%s:%s' % (username, password)).encode('utf-8'))).decode('utf-8')
        request.headers['Proxy-Authorization'] = auth


    def process_response(self, request, response, spider):
        global fail_time, proxy, THRESHOLD
        if not(200 <= response.status < 300):
            fail_time += 1
            if fail_time >= THRESHOLD:
                proxy = fetch_one_proxy()
                fail_time = 0
        return response


# User-Agent中间件
class AgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'
        request.headers.setdefault('User-Agent', ua)

class ScrapyProxySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
