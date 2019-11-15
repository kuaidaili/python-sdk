# -*- coding: utf-8 -*-

"""封装auth对象
    用于保存用户orderid、apiKey，以及计算签名
"""

import base64
import hashlib
import hmac

class Auth:
    """用于保存用户orderid、apiKey，以及计算签名的对象。"""

    def __init__(self, orderId, apiKey):
        self._orderId = orderId
        self._apiKey = apiKey

    @classmethod
    def get_string_to_sign(cls, method, endpoint, params):
        """ 生成签名原文字符串 """
        s = method + endpoint.split('.com')[1] + '?'
        query_str = '&'.join("%s=%s" % (k, params[k]) for k in sorted(params))
        return s + query_str

    def sign_str(self, raw_str, method=hashlib.sha1):
        """ 生成签名串 """
        try:
            hmac_str = hmac.new(self.apiKey.encode('utf8'), raw_str.encode('utf8'), method).digest()
        except UnicodeDecodeError as e:
            hmac_str = hmac.new(self.apiKey.encode('utf8'), raw_str, method).digest()
        return base64.b64encode(hmac_str)

    @property
    def orderId(self):
        return self._orderId

    @property
    def apiKey(self):
        return self._apiKey
