# -*- coding: utf-8 -*-

"""枚举各个api的主机+路径
"""

from enum import Enum, unique


@unique
class EndPoint(Enum):
    """ 各个api的主机+路径 """
    GetOrderExpireTime = "dev.kdlapi.com/api/getorderexpiretime"
    GetIpWhitelist = "dev.kdlapi.com/api/getipwhitelist"  # 获取IP白名单
    SetIpWhitelist = "dev.kdlapi.com/api/setipwhitelist"  # 设置IP白名单
    GetKpsProxy = "kps.kdlapi.com/api/getkps"
    GetDpsProxy = "dps.kdlapi.com/api/getdps"
    GetOpsProxyNormalOrVip = "dev.kdlapi.com/api/getproxy"
    GetOpsProxySvip = "svip.kdlapi.com/api/getproxy"
    GetOpsProxyEnt = "ent.kdlapi.com/api/getproxy"
    CheckDpsValid = "dps.kdlapi.com/api/checkdpsvalid"
    CheckOpsValid = "dev.kdlapi.com/api/checkopsvalid"
    GetIpBalance = "dps.kdlapi.com/api/getipbalance"
    GetDpsValidTime = "dps.kdlapi.com/api/getdpsvalidtime"
    TpsCurrentIp = "tps.kdlapi.com/api/tpscurrentip"  # 获取当前隧道代理IP
    ChangeTpsIp = "tps.kdlapi.com/api/changetpsip"  # 更改当前隧道代理IP
    GetTps = "tps.kdlapi.com/api/gettps"  # 获取隧道代理IP
    GetProxyAuthorization = "dev.kdlapi.com/api/getproxyauthorization"  # 获取代理鉴权信息

    # 工具接口
    GetUA = "www.kuaidaili.com/api/getua"  # 获取User Agent
    GetAreaCode = "dev.kdlapi.com/api/getareacode"  # 获取指定地区编码
    GetAccountBalance = "dev.kdlapi.com/api/getaccountbalance"  # 获取账户余额

    # 订单相关接口
    CreateOrder = "dev.kdlapi.com/api/createorder"   # 创建订单
    GetOrderInfo = "dev.kdlapi.com/api/getorderinfo"  # 获取订单信息
    SetAutoRenew = "dev.kdlapi.com/api/setautorenew"  # 开启/关闭自动续费
    CloseOrder = "dev.kdlapi.com/api/closeorder"  # 关闭订单
    QueryKpsCity = "dev.kdlapi.com/api/querykpscity"  # 查询独享代理城市信息

    GetSecretToken = "auth.kdlapi.com/api/get_secret_token"  # 获取token
