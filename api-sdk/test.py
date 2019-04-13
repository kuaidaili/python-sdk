# -*- coding: utf-8 -*-


from kdl import Auth, Client

import unittest
import time

from kdl.exceptions import KdlException


class TestExpiredKpsOrder(unittest.TestCase):
    def setUp(self):
        self.auth = Auth("904259670668686", "u8n5a0f2hu39o80lpir3hq1kug27tb5i")
        self.client = Client(self.auth)

    def test_get_expire_time(self):
        expire_time = self.client.get_order_expire_time()
        time_struct = time.strptime(expire_time, '%Y-%m-%d %H:%M:%S')
        timestamp = int(time.mktime(time_struct))
        timestamp_now = int(time.time())
        assert timestamp_now > timestamp
        assert isinstance(expire_time, unicode) or isinstance(expire_time.encode('utf8'), str)

    def test_get_ip_whitelist(self):
        iplist = self.client.get_ip_whitelist()
        assert isinstance(iplist, list)

    def test_set_ip_whitelist(self):
        res = self.client.set_ip_whitelist("")
        assert res
        iplist = self.client.get_ip_whitelist()
        assert len(iplist) == 0
        self.client.set_ip_whitelist("127.0.0.1")
        assert len(self.client.get_ip_whitelist()) == 1

    def test_get_proxy(self):
        with self.assertRaises(KdlException):
            self.client.get_kps(1)


if __name__ == '__main__':
    unittest.main()