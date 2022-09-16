# -*- coding: utf-8 -*-

"""python api sdk单元测试
"""

from kdl import Auth, Client

import unittest

from kdl.exceptions import KdlException
import re


secret_id = "o4sfdlk0yfk67vy2ca2b"
secret_key = "v35y327ruqy16vrtl6cejzjbsuljqn3g"



ip_pattern = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
ip_port_pattern = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):\d{2,5}$"
time_pattern = "(((01[0-9]{2}|0[2-9][0-9]{2}|[1-9][0-9]{3})-(0?[13578]|1[02])-(0?[1-9]|[12]\\d|3[01]))|((01[0-9]{2}|0[2-9][0-9]{2}|[1-9][0-9]{3})-(0?[13456789]|1[012])-(0?[1-9]|[12]\\d|30))|((01[0-9]{2}|0[2-9][0-9]{2}|[1-9][0-9]{3})-0?2-(0?[1-9]|1\\d|2[0-8]))|(((1[6-9]|[2-9]\\d)(0[48]|[2468][048]|[13579][26])|((04|08|12|16|[2468][048]|[3579][26])00))-0?2-29)) (20|21|22|23|[0-1]?\\d):[0-5]?\\d:[0-5]?\\d"


def is_valid_str(str, pattern):
    """判断格式是否正确"""
    if str and re.match(pattern, str):
        return True
    return False


def is_valid_ip_list(lis, pattern):
    """判断返回的ip列表或者ip加端口列表是否格式正确"""
    if not lis:
        return True

    for i in lis:
        flag = is_valid_str(i, pattern)
        if not flag :
            return False
    return True


class TestBase(unittest.TestCase):
    """单元测试基类，所有单元测试类从此类继承"""

    name = "单元测试"

    @classmethod
    def setUpClass(cls):
        print('%s测试开始' % cls.name)

    @classmethod
    def tearDownClass(cls):
        print('%s测试结束' % cls.name)

    def setUp(self):
        self.auth = Auth(secret_id, secret_key)
        self.client = Client(self.auth)

    def test_get_expire_time(self):
        """ 获取订单过期时间 """
        expire_time = self.client.get_order_expire_time(sign_type='token')
        # assert isinstance(expire_time, unicode) or isinstance(expire_time, str)
        print(expire_time)
        assert isinstance(expire_time, str) and is_valid_str(expire_time,time_pattern)


class TestBase2(TestBase):
    """具有获取IP白名单api和设置IP白名单的api,获取鉴权信息api的类，
        目前只有私密代理，独享代理，隧道代理"""

    def test_get_ip_whitelist(self):
        """ 获取ip白名单 """
        ip_whitelist = self.client.get_ip_whitelist()
        print(ip_whitelist)
        assert isinstance(ip_whitelist, list) and is_valid_ip_list(ip_whitelist,ip_pattern)

    def test_set_ip_whitelist(self):
        """ 设置ip白名单 """
        self.client.set_ip_whitelist([])
        ip_whitelist = self.client.get_ip_whitelist()
        assert len(ip_whitelist) == 0
        set_ip_list = ["171.113.144.44", "171.113.244.41"]
        self.client.set_ip_whitelist(set_ip_list)
        ip_whitelist = self.client.get_ip_whitelist()
        set_ip_list.reverse()
        assert len(ip_whitelist) == 2 and isinstance(ip_whitelist, list) and is_valid_ip_list(ip_whitelist,ip_pattern) and ip_whitelist == set_ip_list
        self.client.set_ip_whitelist([])

    def test_get_proxy_authorization(self):
        data = self.client.get_proxy_authorization(plain_text=1, sign_type='token')
        assert isinstance(data, dict)
        print(data)


class TestDpsOrder(TestBase2):
    """ 私密代理 """

    name = "私密代理测试"

    def test_get_proxy(self):
        """ 获取私密代理 """
        ips = self.client.get_dps(2, sign_type='token', format='text', area='云南,广东', pt=2, f_citycode=1)
        # ips = self.client.get_dps(2, format='text')
        print(ips)
        assert isinstance(ips, list) or isinstance(ips, str) or isinstance(ips.encode('utf8'), str) or isinstance(ips.encode('utf8'), bytes)  and is_valid_ip_list(ips,ip_port_pattern)

    def test_check_dps_valid(self):
        """检测是否有效"""
        ips = self.client.get_dps(2, format='json', area='北京，上海')
        print(ips)
        is_valid = self.client.check_dps_valid(ips)
        assert isinstance(is_valid, dict)

    def test_get_ip_balance(self):
        """检测还剩多少ip地址可以提取"""
        balance = self.client.get_ip_balance()
        assert isinstance(balance, int)

    def test_get_dps_valid_time(self):
        ips = self.client.get_dps(5, format='json', sign_type="hmacsha1")
        print("ips: ", ips)
        seconds = self.client.get_dps_valid_time(ips, sign_type="hmacsha1")
        print("seconds: ", seconds)
        assert isinstance(seconds, dict)

    def test_get_secret_token(self):
        secret_token = self.client.get_secret_token()
        print(secret_token)
   

class TestKpsOrder(TestBase):
    """ 独享代理 """
    name = '独享代理'

    def test_get_proxy(self):
        """ 获取私密代理 """
        ips = self.client.get_kps(2, sign_type='hmacsha1', format='json', area='云南,广东', pt=2, f_citycode=1)
        assert isinstance(ips, list) or isinstance(ips, str) or isinstance(ips.encode('utf8'), str) or isinstance(ips.encode('utf8'), bytes) and  is_valid_ip_list(ips,ip_port_pattern)

    def test_check_dps_valid(self):
        """检测是否有效"""
        ips = self.client.get_kps(2, format='json', area='北京', pt=2)
        with self.assertRaises(KdlException):
            self.client.check_dps_valid(ips)

    def test_get_ip_balance(self):
        """检测还剩多少ip地址可以提取"""
        with self.assertRaises(KdlException):
            self.client.get_ip_balance()

class TestOpsOrder(TestBase):
    """ 开放代理 """

    name = '开放代理'

    def test_get_ip_whitelist(self):
        """ 获取ip白名单 """
        with self.assertRaises(KdlException):
            self.client.get_ip_whitelist()

    def test_get_proxy(self):
        """ 获取私密代理 """
        ips = self.client.get_proxy(2, order_level='vip', sign_type='hmacsha1', format='json', area='云南,广东', pt=2,
                                    f_citycode=1)
        assert isinstance(ips, list) or isinstance(ips, str) or isinstance(ips.encode('utf8'), str) or isinstance(ips.encode('utf8'), bytes)  and  is_valid_ip_list(ips,ip_port_pattern)

    def test_check_ops_valid(self):
        """检测是否有效"""
        ips = self.client.get_proxy(2, format='json', area='北京', pt=2)
        is_valid = self.client.check_ops_valid(ips)
        assert isinstance(is_valid, dict)

    def test_get_ip_balance(self):
        """检测还剩多少ip地址可以提取"""
        with self.assertRaises(KdlException):
            self.client.get_ip_balance()

class TestTpsOrder(TestBase2):
    name = "隧道代理"

    def test_get_tps_ip(self):
        """获取当前隧道ip"""
        current_ip = self.client.tps_current_ip(sign_type='hmacsha1')
        assert len(current_ip) == 0 or (len(current_ip.split('.')) == 4 and is_valid_str(current_ip,ip_pattern))

    def test_change_tcp_ip(self):
        """立即改变隧道ip"""
        new_ip = self.client.change_tps_ip()
        assert len(new_ip.split('.')) == 4 and is_valid_str(new_ip,ip_pattern)

    def test_get_tps(self):
        tps_list = self.client.get_tps(2,sign_type='hmacsha1', format='json')
        assert isinstance(tps_list, list)
    


class TestExpiredKpsOrder(unittest.TestCase):
    """ 过期订单 """

    name = "过期订单"

    def test_get_expire_time(self):
        with self.assertRaises(KdlException):
            self.client.get_order_expire_time()

    def test_get_ip_whitelist(self):
        with self.assertRaises(KdlException):
            self.client.get_ip_whitelist()

    def test_set_ip_whitelist(self):
        with self.assertRaises(KdlException):
            self.client.set_ip_whitelist("127.0.0.1")

    def test_get_proxy(self):
        with self.assertRaises(KdlException):
            self.client.get_kps(1)


class TestNoApiKeyOrder(unittest.TestCase):
    """ 不提供apiKey，仅能成功调用不需要signature的api """
    name = "不提供apiKey，仅能成功调用不需要signature的api "

    def test_get_ip_whitelist(self):
        """ 获取ip白名单 """
        with self.assertRaises(NameError):
            self.client.get_ip_whitelist()

    def test_get_proxy(self):
        """ 获取私密代理 """
        with self.assertRaises(NameError):
            self.client.get_proxy(2, order_level='vip', sign_type='hmacsha1', format='json', area='云南,广东', pt=2,
                                  f_citycode=1)
        with self.assertRaises(NameError):
            self.client.get_proxy(2, order_level='vip', sign_type='simple', format='json', area='云南,广东', pt=2,
                                  f_citycode=1)
        ips = self.client.get_proxy(2, order_level='vip', format='json', area='云南,广东', pt=2,
                                    f_citycode=1)

        assert isinstance(ips, list) and is_valid_ip_list(ips,ip_port_pattern)


    def test_check_ops_valid(self):
        ips = self.client.get_proxy(2, format='json', area='北京', pt=2)
        with self.assertRaises(NameError):
            is_valid = self.client.check_ops_valid(ips)
            assert isinstance(is_valid, dict)

    def test_get_ip_balance(self):
        with self.assertRaises(NameError):
            self.client.get_ip_balance()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTpsOrder)
    unittest.TextTestRunner(verbosity=2).run(suite)

