# -*- coding: utf-8 -*-


from kdl import Auth, Client

import unittest

from kdl.exceptions import KdlException


class TestDpsOrder(unittest.TestCase):
    """ 私密代理 """

    def setUp(self):
        self.auth = Auth(orderid, apiKey)
        self.client = Client(self.auth)

    def test_get_expire_time(self):
        """ 获取订单过期时间 """
        expire_time = self.client.get_order_expire_time(sign_type='hmacsha1')
        # assert isinstance(expire_time, unicode) or isinstance(expire_time, str)
        assert isinstance(expire_time, str) or isinstance(expire_time.encode('utf8'), str) or isinstance(expire_time.encode('utf8'), bytes)

    def test_get_ip_whitelist(self):
        """ 获取ip白名单 """
        ip_whitelist = self.client.get_ip_whitelist(sign_type='hmacsha1')
        assert isinstance(ip_whitelist, list)

    def test_set_ip_whitelist(self):
        """ 设置ip白名单 """
        self.client.set_ip_whitelist([], sign_type='hmacsha1')
        ip_whitelist = self.client.get_ip_whitelist()
        assert len(ip_whitelist) == 0
        self.client.set_ip_whitelist(["10.31.89.93", "1.2.3.4"], sign_type='hmacsha1')
        ip_whitelist = self.client.get_ip_whitelist(sign_type='simple')
        assert len(ip_whitelist) == 2
        self.client.set_ip_whitelist([], sign_type='simple')

    def test_get_proxy(self):
        """ 获取私密代理 """
        ips = self.client.get_dps(2, sign_type='hmacsha1', format='text', area='云南,广东', pt=2, f_citycode=1)
        # ips = self.client.get_dps(2, format='text')
        print(ips)
        assert isinstance(ips, list) or isinstance(ips, str) or isinstance(ips.encode('utf8'), str) or isinstance(ips.encode('utf8'), bytes)

    def test_check_dps_valid(self):
        ips = self.client.get_dps(2, format='json', area='北京，上海')
        print(ips)
        is_valid = self.client.check_dps_valid(ips)
        assert isinstance(is_valid, dict)

    def test_get_ip_balance(self):
        balance = self.client.get_ip_balance()
        assert isinstance(balance, int)


class TestKpsOrder(unittest.TestCase):
    """ 独享代理 """

    def setUp(self):
        self.auth = Auth(orderid, apiKey)
        self.client = Client(self.auth)

    def test_get_expire_time(self):
        """ 获取订单过期时间 """
        expire_time = self.client.get_order_expire_time()
        assert isinstance(expire_time, str) or isinstance(expire_time.encode('utf8'), str) or isinstance(expire_time.encode('utf8'), bytes)


    def test_get_ip_whitelist(self):
        """ 获取ip白名单 """
        ip_whitelist = self.client.get_ip_whitelist()
        assert isinstance(ip_whitelist, list)

    def test_set_ip_whitelist(self):
        """ 设置ip白名单 """
        ip_whitelist = self.client.get_ip_whitelist()
        assert len(ip_whitelist) == 0
        self.client.set_ip_whitelist(["10.31.89.93", "1.2.3.4"])
        ip_whitelist = self.client.get_ip_whitelist()
        assert len(ip_whitelist) == 2 and isinstance(ip_whitelist, list)
        self.client.set_ip_whitelist([])

    def test_get_proxy(self):
        """ 获取私密代理 """
        ips = self.client.get_kps(2, sign_type='hmacsha1', format='json', area='云南,广东', pt=2, f_citycode=1)
        assert isinstance(ips, list) or isinstance(ips, str) or isinstance(ips.encode('utf8'), str) or isinstance(ips.encode('utf8'), bytes)

    def test_check_dps_valid(self):
        ips = self.client.get_kps(2, format='json', area='北京', pt=2)
        with self.assertRaises(KdlException):
            self.client.check_dps_valid(ips)

    def test_get_ip_balance(self):
        with self.assertRaises(KdlException):
            self.client.get_ip_balance()


class TestOpsOrder(unittest.TestCase):
    """ 开放代理 """

    def setUp(self):
        self.auth = Auth(orderid, apiKey)
        self.client = Client(self.auth)

    def test_get_expire_time(self):
        """ 获取订单过期时间 """
        expire_time = self.client.get_order_expire_time()
        assert isinstance(expire_time, str) or isinstance(expire_time.encode('utf8'), str) or isinstance(expire_time.encode('utf8'), bytes)


    def test_get_ip_whitelist(self):
        """ 获取ip白名单 """
        with self.assertRaises(KdlException):
            self.client.get_ip_whitelist()

    def test_get_proxy(self):
        """ 获取私密代理 """
        ips = self.client.get_proxy(2, order_level='vip', sign_type='hmacsha1', format='json', area='云南,广东', pt=2,
                                    f_citycode=1)
        assert isinstance(ips, list) or isinstance(ips, str) or isinstance(ips.encode('utf8'), str) or isinstance(ips.encode('utf8'), bytes)


    def test_check_ops_valid(self):
        ips = self.client.get_proxy(2, format='json', area='北京', pt=2)
        is_valid = self.client.check_ops_valid(ips)
        assert isinstance(is_valid, dict)

    def test_get_ip_balance(self):
        with self.assertRaises(KdlException):
            self.client.get_ip_balance()


class TestExpiredKpsOrder(unittest.TestCase):
    """ 过期订单 """

    def setUp(self):
        self.auth = Auth(orderid, apiKey)
        self.client = Client(self.auth)

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

    def setUp(self):
        self.auth = Auth(orderid)
        self.client = Client(self.auth)

    def test_get_expire_time(self):
        """ 获取订单过期时间 """
        with self.assertRaises(NameError):
            self.client.get_order_expire_time()

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
        assert isinstance(ips, list)

    def test_check_ops_valid(self):
        ips = self.client.get_proxy(2, format='json', area='北京', pt=2)
        with self.assertRaises(NameError):
            is_valid = self.client.check_ops_valid(ips)
            assert isinstance(is_valid, dict)

    def test_get_ip_balance(self):
        with self.assertRaises(NameError):
            self.client.get_ip_balance()


if __name__ == '__main__':
    unittest.main()
