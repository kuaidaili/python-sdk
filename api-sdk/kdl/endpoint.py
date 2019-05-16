# -*- coding: utf-8 -*-

from enum import Enum, unique


@unique
class EndPoint(Enum):
    """ 各个api的主机+路径 """
    GetOrderExpireTime = "dev.kdlapi.com/api/getorderexpiretime"
    GetIpWhitelist = "dev.kdlapi.com/api/getipwhitelist"
    SetIpWhitelist = "dev.kdlapi.com/api/setipwhitelist"
    GetKpsProxy = "kps.kdlapi.com/api/getkps"
    GetDpsProxy = "dps.kdlapi.com/api/getdps"
    GetOpsProxyNormalOrVip = "dev.kdlapi.com/api/getproxy"
    GetOpsProxySvip = "svip.kdlapi.com/api/getproxy"
    GetOpsProxyEnt = "ent.kdlapi.com/api/getproxy"
    CheckDpsValid = "dps.kdlapi.com/api/checkdpsvalid"
    CheckOpsValid = "dev.kdlapi.com/api/checkopsvalid"
    GetIpBalance = "dps.kdlapi.com/api/getipbalance"