# -*- coding: utf-8 -*-
import json
import time
import requests

from kdl.endpoint import EndPoint
from kdl.exceptions import KdlException, KdlNameError, KdlTypeError, KdlStatusError
from kdl.utils import hmac_required, OpsOrderLevel


class Client:
    def __init__(self, auth):
        self.auth = auth

    @hmac_required
    def get_order_expire_time(self):
        """获取订单到期时间
        强制hmac验证 """
        endpoint = EndPoint.GetOrderExpireTime.value
        params = self._get_params(endpoint)
        res = self._get_base_res("GET", endpoint, params)
        return res['data']['expire_time']

    @hmac_required
    def get_ip_whitelist(self):
        """ 获取订单的ip白名单, 强制hmac验证 """
        endpoint = EndPoint.GetIpWhitelist.value
        params = self._get_params(endpoint)
        res = self._get_base_res("GET", endpoint, params)
        return res['data']['ipwhitelist']

    @hmac_required
    def set_ip_whitelist(self, iplist=None):
        """ 设置订单的ip白名单, 强制hmac验证 """
        if iplist is None:
            raise KdlNameError("miss param: iplist")
        if not (isinstance(iplist, list) or isinstance(iplist, tuple) or isinstance(iplist, str)):
            raise KdlTypeError("iplist should be a instance of list or tuple or str")
        if isinstance(iplist, list) or isinstance(iplist, tuple):
            iplist = ', '.join(iplist)
        endpoint = EndPoint.SetIpWhitelist.value
        params = self._get_params(endpoint, iplist=iplist)
        self._get_base_res("POST", endpoint, params)
        return True

    def get_dps(self, num=None, sign_type="simple", **kwargs):
        """
            获取私密代理, 默认simple鉴权
            :return 若为json格式, 则返回 data部分
            :return 若为text/xml 格式, 则原样返回
        """
        if num is None:
            raise KdlNameError("miss param: num")
        endpoint = EndPoint.GetDpsProxy.value
        params = self._get_params(endpoint, sign_type, num=num, **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']
        return res

    @hmac_required
    def check_dps_valid(self, proxy, **kwargs):
        """
            检测私密代理有效性, 强制hmacsha1验证
            :return 返回data部分, 格式为：ip: true/false
        """
        if not proxy:
            raise KdlNameError("miss param: proxy")
        if not (isinstance(proxy, list) or isinstance(proxy, tuple) or isinstance(proxy, str)):
            raise KdlTypeError("proxy should be a instance of list or tuple or str")
        if isinstance(proxy, list) or isinstance(proxy, tuple):
            proxy = ', '.join(proxy)
        endpoint = EndPoint.CheckDpsValid.value
        params = self._get_params(endpoint, proxy=proxy)
        res = self._get_base_res("GET", endpoint, params)
        return res['data']

    @hmac_required
    def get_ip_balance(self):
        """
            获取计数版订单ip余额, 强制hmac验证
            :return 返回data中的balance字段, int类型
        """
        endpoint = EndPoint.GetIpBalance.value
        params = self._get_params(endpoint)
        res = self._get_base_res("GET", endpoint, params)
        return res['data']['balance']

    def get_kps(self, num=None, sign_type="simple", **kwargs):
        """ 获取独享代理, 默认simple鉴权 """
        if num is None:
            raise KdlNameError("miss param: num")
        endpoint = EndPoint.GetKpsProxy.value
        params = self._get_params(endpoint, sign_type, num=num, **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']
        return res

    def get_proxy(self, num=None, sign_type="simple", order_level=OpsOrderLevel.NORMAL, **kwargs):
        """获取开放代理
        默认simple鉴权 """
        if num is None:
            raise KdlNameError("miss param: num")
        endpoint = EndPoint.GetOpsProxyNormalOrVip.value
        if order_level == OpsOrderLevel.SVIP:
            endpoint = EndPoint.GetOpsProxySvip.value
        if order_level == OpsOrderLevel.PRO:
            endpoint = EndPoint.GetOpsProxyEnt.value
        params = self._get_params(endpoint, sign_type, num=num, **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']
        return res

    def _get_params(self, endpoint, sign_type="hmacsha1", **kwargs):
        """ 构造请求参数 """
        params = dict(timestamp=int(time.time()), sign_type=sign_type, orderid=self.auth.orderId)
        if endpoint == EndPoint.SetIpWhitelist.value:
            iplist = kwargs.get('iplist')
            params['iplist'] = iplist
            raw_str = self.auth.get_string_to_sign("POST", endpoint, params)
            params["signature"] = self.auth.sign_str(raw_str)
            return params
        elif endpoint == EndPoint.GetDpsProxy.value or endpoint == EndPoint.GetKpsProxy.value or \
                endpoint == EndPoint.GetOpsProxy.value:
            params.update(kwargs)
            if sign_type == "simple":
                return params
        elif endpoint == EndPoint.CheckDpsValid.value:
            proxy = kwargs.get('proxy')
            params['proxy'] = proxy
        raw_str = self.auth.get_string_to_sign("GET", endpoint, params)
        params["signature"] = self.auth.sign_str(raw_str)
        return params

    def _get_base_res(self, method, endpoint, params):
        """ 处理基础请求, 返回请求结果dict """
        try:
            r = None
            if method == "GET":
                r = requests.get("http://" + endpoint, params=params)
            elif method == "POST":
                r = requests.post("http://" + endpoint, data=params)
            if r.status_code != 200:
                raise KdlStatusError(r.status_code, r.content.decode('utf8'))

            try:
                r = json.loads(r.content.decode('utf8'))
                code, msg = r['code'], r['msg']
                if code != 0:
                    raise KdlException(code, msg)
                return r
            except ValueError as e:
                if r.content.strip().startswith("ERROR"):
                    raise KdlException(-3, r.content)
                return r.content.decode('utf8')
        except Exception as e:
            raise e
