# -*- coding: utf-8 -*-

"""将快代理所有api接口封装到Client
"""

import json
import os
import time
import requests
from requests.adapters import HTTPAdapter

from kdl.endpoint import EndPoint
from kdl.exceptions import KdlException, KdlNameError, KdlTypeError, KdlStatusError
from kdl.utils import OpsOrderLevel


SECRET_PATH = './.secret'


class Client:
    def __init__(self, auth, timeout=None, max_retries=None):
        self.auth = auth
        self.session = requests.Session()
        self.timeout = timeout or (6, 8)  # default (connect_timeout, read_timeout)
        self.max_retries = max_retries

    def get_order_expire_time(self, sign_type="token", timeout=None, max_retries=None):
        """获取订单到期时间, 强制签名验证
           :return 订单过期时间字符串
        """

        endpoint = EndPoint.GetOrderExpireTime.value
        params = self._get_params(endpoint, sign_type=sign_type, timeout=timeout, max_retries=max_retries)
        res = self._get_base_res("GET", endpoint, params)

        if isinstance(res, dict):
            return res['data']['expire_time']
        return res

    def get_proxy_authorization(self, plain_text=0, sign_type="token", timeout=None, max_retries=None):
        """获取指定订单访问代理IP的鉴权信息。
        鉴权信息包含用户名密码，用于请求私密代理/独享代理/隧道代理时进行身份验证。
            :return 返回信息的字典
        """
        endpoint = EndPoint.GetProxyAuthorization.value
        params = self._get_params(endpoint, plaintext=plain_text, sign_type=sign_type, timeout=timeout, max_retries=max_retries)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']
        return res

    def get_ip_whitelist(self, sign_type="token", timeout=None, max_retries=None):
        """获取订单的ip白名单, 强制签名验证
           :return ip白名单列表
        """
        endpoint = EndPoint.GetIpWhitelist.value
        params = self._get_params(endpoint, sign_type=sign_type, timeout=timeout, max_retries=max_retries)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']['ipwhitelist']
        return res

    def set_ip_whitelist(self, iplist=None, sign_type="token", timeout=None, max_retries=None):
        """设置订单的ip白名单, 强制签名验证
           :param iplist参数类型为 str 或 list 或 tuple
                  如果为字符串则ip之间用逗号隔开
           :return 成功则返回True, 否则抛出异常
        """

        if iplist is None:
            raise KdlNameError("miss param: iplist")
        if not (isinstance(iplist, list) or isinstance(iplist, tuple) or isinstance(iplist, str)):
            raise KdlTypeError("iplist type error, should be a instance of list or tuple or str")
        if isinstance(iplist, list) or isinstance(iplist, tuple):
            iplist = ','.join(iplist)
        endpoint = EndPoint.SetIpWhitelist.value
        params = self._get_params(endpoint, iplist=iplist, sign_type=sign_type, timeout=timeout, max_retries=max_retries)
        self._get_base_res("POST", endpoint, params)
        return True

    def tps_current_ip(self, sign_type="token", timeout=None, max_retries=None):
        """仅支持支持换IP周期>=1分钟的隧道代理订单
           获取隧道当前的IP，默认“token”鉴权
           :param sign_type:默认token
           :return:返回ip地址。
        """
        endpoint = EndPoint.TpsCurrentIp.value
        params = self._get_params(endpoint, sign_type=sign_type, timeout=timeout, max_retries=max_retries)
        res = self._get_base_res("GET", endpoint, params)
        return res['data']['current_ip']

    def change_tps_ip(self, sign_type="token", timeout=None, max_retries=None):
        """仅支持支持换IP周期>=1分钟的隧道代理订单
           :param sign_type: 默认token
           :return: 返回新的IP地址
        """
        endpoint = EndPoint.ChangeTpsIp.value
        params = self._get_params(endpoint, sign_type=sign_type, timeout=timeout, max_retries=max_retries)
        res = self._get_base_res("GET", endpoint, params)
        return res['data']['new_ip']

    def get_tps(self, num=None, sign_type="token", **kwargs):
        """获取隧道代理IP, 默认"token"鉴权 https://www.kuaidaili.com/doc/api/gettps/
           :param num : 提取数量，int类型
           :param kwargs: 其他关键字参数，具体有那些参数请查看帮助中心api说明
           :return 若为json格式, 则返回data中proxy_list部分, 即proxy列表, 否则原样返回
        """
        if num is None:
            raise KdlNameError("miss param: num")
        if not isinstance(num, int):
            KdlTypeError("num should be a integer")
        endpoint = EndPoint.GetTps.value
        params = self._get_params(endpoint, num=num, sign_type=sign_type, **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']['proxy_list']
        return res

    def get_dps_valid_time(self, proxy=None, sign_type="token", **kwargs):
        """获取私密代理ip有效时间
           :param proxy: 私密代理列表, 格式： IP:PORT, eg: 113.120.61.166:22989,122.4.44.132:21808
           :param sign_type: 认证方式
           :return: 返回data部分, 格式为由'proxy: seconds(剩余秒数)'组成的列表
        """
        if not proxy:
            raise KdlNameError("miss param: proxy")
        if not (isinstance(proxy, list) or isinstance(proxy, tuple) or isinstance(proxy, str)):
            raise KdlTypeError("proxy should be a instance of list or tuple or str")
        if isinstance(proxy, list) or isinstance(proxy, tuple):
            proxy = ','.join(proxy)
        endpoint = EndPoint.GetDpsValidTime.value
        params = self._get_params(endpoint, proxy=proxy, sign_type=sign_type)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']
        return res

    def get_dps(self, num=None, sign_type="token", **kwargs):
        """获取私密代理, 默认"token"鉴权
           :param num: 提取数量, int类型
           :param kwargs: 其他关键字参数，具体有那些参数请查看帮助中心api说明
           :return 若为json格式, 则返回data中proxy_list部分, 即proxy列表, 否则原样返回
        """
        if num is None:
            raise KdlNameError("miss param: num")
        if not isinstance(num, int):
            KdlTypeError("num should be a integer")
        endpoint = EndPoint.GetDpsProxy.value
        params = self._get_params(endpoint, num=num, sign_type=sign_type, **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']['proxy_list']
        return res

    def check_dps_valid(self, proxy=None, sign_type="token", **kwargs):
        """检测私密代理有效性, 强制签名验证
           :return 返回data部分, 格式为由'proxy: True/False'组成的dict
        """
        if not proxy:
            raise KdlNameError("miss param: proxy")
        if not (isinstance(proxy, list) or isinstance(proxy, tuple) or isinstance(proxy, str) or isinstance(proxy, unicode)):
            raise KdlTypeError("proxy should be a instance of list or tuple or str")
        if isinstance(proxy, list) or isinstance(proxy, tuple):
            proxy = ','.join(proxy)
        endpoint = EndPoint.CheckDpsValid.value
        params = self._get_params(endpoint, proxy=proxy, sign_type=sign_type)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']
        return res

    def get_ip_balance(self, sign_type="token", timeout=None, max_retries=None):
        """获取计数版订单ip余额, 强制签名验证,
           此接口只对按量付费订单和包年包月的集中提取型订单有效
           :return 返回data中的balance字段, int类型
        """
        endpoint = EndPoint.GetIpBalance.value
        params = self._get_params(endpoint, sign_type=sign_type, timeout=timeout, max_retries=max_retries)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']['balance']
        return res

    def get_kps(self, num=None, sign_type="token", **kwargs):
        """获取独享代理, 默认"token"鉴权
           :param num: 提取数量, sign_type: 鉴权方式
           :param kwargs: 其他关键字参数，具体有那些参数请查看帮助中心api说明
           :return 若为json格式, 则返回data中proxy_list部分, 即proxy列表, 否则原样返回
        """
        if num is None:
            raise KdlNameError("miss param: num")
        if not isinstance(num, int):
            KdlTypeError("num should be a integer")
        endpoint = EndPoint.GetKpsProxy.value
        params = self._get_params(endpoint, num=num, sign_type=sign_type, **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']['proxy_list']
        return res

    def get_proxy(self, num=None, order_level=OpsOrderLevel.NORMAL, sign_type="token", **kwargs):
        """获取开放代理, 默认不需要鉴权
           :param num: 提取数量, sign_type: 鉴权方式, order_level: 开放代理订单类型
           :param kwargs: 其他关键字参数，具体有那些参数请查看帮助中心api说明
           :return 若为json格式, 则返回data中proxy_list部分, 即proxy列表, 否则原样返回
        """
        if num is None:
            raise KdlNameError("miss param: num")
        if not isinstance(num, int):
            KdlTypeError("num should be a integer")
        endpoint = EndPoint.GetOpsProxyNormalOrVip.value
        if order_level == OpsOrderLevel.SVIP:
            endpoint = EndPoint.GetOpsProxySvip.value
        if order_level == OpsOrderLevel.PRO:
            endpoint = EndPoint.GetOpsProxyEnt.value

        params = self._get_params(endpoint, num=num, sign_type=sign_type, **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']['proxy_list']
        return res

    def check_ops_valid(self, proxy=None, sign_type="token", **kwargs):
        """检测开放代理有效性, 强制签名验证
           :return 返回data部分, 格式为由'proxy: True/False'组成的列表
        """
        if not proxy:
            raise KdlNameError("miss param: proxy")
        if not (isinstance(proxy, list) or isinstance(proxy, tuple) or isinstance(proxy, str)):
            raise KdlTypeError("proxy should be a instance of list or tuple or str")
        if isinstance(proxy, list) or isinstance(proxy, tuple):
            proxy = ','.join(proxy)
        endpoint = EndPoint.CheckOpsValid.value
        params = self._get_params(endpoint, proxy=proxy, sign_type=sign_type)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']
        return res

    def get_ua(self, num=1, **kwargs):
        """获取User Agent
           :return 若为json格式, 则返回data中ua_list部分, 即user agent列表, 否则原样返回
        """
        endPoint = EndPoint.GetUA.value
        params = self._get_params(endPoint, num=num, sign_type="token", **kwargs)
        res = self._get_base_res("GET", endPoint, params)
        if isinstance(res, dict):
            return res['data']["ua_list"]
        return res

    def get_area_code(self, area, **kwargs):
        """获取指定地区编码
           :return:
        """
        endpoint = EndPoint.GetAreaCode.value
        params = self._get_params(endpoint, area=area, sign_type="token", **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']
        return res

    def get_account_balance(self, **kwargs):
        """获取账户余额
           :return:
        """
        endpoint = EndPoint.GetAccountBalance.value
        params = self._get_params(endpoint, sign_type="token", **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        if isinstance(res, dict):
            return res['data']
        return res

    def create_order(self, product, pay_type, **kwargs):
        """创建订单，自动从账户余额里结算费用
           :return:
        """
        if not (product and pay_type):
            raise KdlNameError('miss param: product or pay_type')
        endpoint = EndPoint.CreateOrder.value
        params = self._get_params(endpoint,product=product, pay_type=pay_type, sign_type="hmacsha1", **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        return res

    def get_order_info(self, **kwargs):
        """获取订单的详细信息
           :return:
        """
        endpoint = EndPoint.GetOrderInfo.value
        params = self._get_params(endpoint, sign_type="hmacsha1", **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        return res

    def set_auto_renew(self, autorenew, **kwargs):
        """开启/关闭自动续费
           :return:
        """
        if not autorenew:
            raise KdlNameError('miss param: autorenew')
        endpoint = EndPoint.SetAutoRenew.value
        params = self._get_params(endpoint, autorenew=autorenew, sign_type="hmacsha1", **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        return res

    def close_order(self, **kwargs):
        """关闭指定订单, 此接口只对按量付费(后付费)订单有效
           :return:
        """
        endpoint = EndPoint.CloseOrder.value
        params = self._get_params(endpoint, sign_type="hmacsha1", **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        return res

    def query_kps_city(self, serie, **kwargs):
        """查询独享代理有哪些城市可供开通。对于IP共享型还可查询到每个城市可开通的IP数量。
           :return:
        """
        if not serie:
            raise KdlNameError('miss params: serie')
        endpoint = EndPoint.QueryKpsCity.value
        params = self._get_params(endpoint, serie=serie, sign_type="hmacsha1", **kwargs)
        res = self._get_base_res("GET", endpoint, params)
        return res

    def _get_secret_token(self, timeout=None, max_retries=None):
        try:
            timeout = timeout or self.timeout
            max_retries = max_retries or self.max_retries
            self.session.mount('http://', HTTPAdapter(max_retries=max_retries))
            self.session.mount('https://', HTTPAdapter(max_retries=max_retries))
            r = self.session.post(url='https://' + EndPoint.GetSecretToken.value,
                                  data={'secret_id': self.auth.secret_id, 'secret_key': self.auth.secret_key},
                                  timeout=timeout)
            if r.status_code != 200:
                raise KdlStatusError(r.status_code, r.content.decode('utf8'))
        except requests.exceptions.RequestException as e:
            pass  # TODO: 重试后失败 处理
            raise e

        res = json.loads(r.content.decode('utf8'))
        code, msg = res['code'], res['msg']
        if code != 0:
            raise KdlException(code, msg)
        secret_token = res['data']['secret_token']
        expire = str(res['data']['expire'])
        _time = '%.6f' % time.time()
        return secret_token, expire, _time

    def _read_secret_token(self):
        with open(SECRET_PATH, 'r') as f:
            token_info = f.read()
        secret_token, expire, _time = token_info.split('|')
        if float(_time) + float(expire) - 3 * 60 < time.time():  # 还有3分钟过期时更新
            secret_token, expire, _time = self._get_secret_token()
            with open(SECRET_PATH, 'w') as f:
                f.write(secret_token + '|' + expire + '|' + _time)
        return secret_token

    def get_secret_token(self):
        if os.path.exists(SECRET_PATH):
            secret_token = self._read_secret_token()
        else:
            secret_token, expire, _time = self._get_secret_token()
            with open(SECRET_PATH, 'w') as f:
                f.write(secret_token + '|' + expire + '|' + _time)
        return secret_token

    def _get_params(self, endpoint, **kwargs):
        """构造请求参数"""
        params = dict(secret_id=self.auth.secret_id)
        params.update(kwargs)

        sign_type = kwargs.get('sign_type', None)
        if not sign_type:
            return params

        if not self.auth.secret_key:
            raise KdlNameError("secret_key is required for signature")

        if sign_type == "hmacsha1":
            params['timestamp'] = int(time.time())
            if endpoint == EndPoint.SetIpWhitelist.value:
                raw_str = self.auth.get_string_to_sign("POST", endpoint, params.copy())
            else:
                raw_str = self.auth.get_string_to_sign("GET", endpoint, params.copy())
            params["signature"] = self.auth.sign_str(raw_str)
        elif sign_type == "token":
            secret_token = self.get_secret_token()
            params['signature'] = secret_token
        else:
            raise KdlNameError("unknown sign_type {}".format(sign_type))

        return params

    def _get_base_res(self, method, endpoint, params):
        """处理基础请求,
           若响应为json格式则返回请求结果dict
           否则直接返回原格式
        """
        try:
            r = None
            timeout = params.get('timeout', '') or self.timeout
            max_retries = params.get('max_retries', '') or self.max_retries
            self.session.mount('http://', HTTPAdapter(max_retries=max_retries))
            self.session.mount('https://', HTTPAdapter(max_retries=max_retries))
            self.auth.clear_req_params(params)

            if method == "GET":
                r = requests.get("https://" + endpoint, params=params, timeout=timeout)
            elif method == "POST":
                r = requests.post("https://" + endpoint, data=params, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=timeout)
            if r.status_code != 200:
                raise KdlStatusError(r.status_code, r.content.decode('utf8'))
            try:
                res = json.loads(r.content.decode('utf8'))
                code, msg = res['code'], res['msg']
                if code != 0:
                    raise KdlException(code, msg)
                return res

            except ValueError as e:
                # 返回结果不是json格式, 直接返回
                if r.content.decode('utf8').strip().startswith("ERROR"):
                    raise KdlException(-3, r.content)
                return r.content.decode('utf8')
        except Exception as e:
            raise e
