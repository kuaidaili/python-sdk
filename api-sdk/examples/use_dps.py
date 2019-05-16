# -*- coding: utf-8 -*-

"""
    私密代理使用示例
    方法的默认鉴权方式请参考帮助中心api文档: "https://help.kuaidaili.com/api/intro/"
    所有方法均可添加关键字参数sign_type修改鉴权方式, 目前有 "simple" 和 "hmacsha1" 两种
    若需要使用鉴权，则auth对象必须将订单号对应的api key作为第二个参数传入构造函数中，否则只能调用
    不需要鉴权的api，比如提取代理的api
"""

import kdl

auth = kdl.Auth("yourorderid", "yourorderapikey")
client = kdl.Client(auth)

# 获取订单到期时间, 返回时间字符串
expire_time = client.get_order_expire_time()
print("expire time", expire_time)

# 获取ip白名单, 返回ip列表
ip_whitelist = client.get_ip_whitelist()
print("ip whitelist", ip_whitelist)

# 设置ip白名单，参数类型为字符串或列表或元组
# 成功则返回True, 否则抛出异常
client.set_ip_whitelist([])
client.set_ip_whitelist("127.0.0.1, 192.168.0.139")
print(client.get_ip_whitelist())
client.set_ip_whitelist(tuple())

# 提取私密代理ip, 第一个参数为提取的数量, 其他参数以关键字参数的形式传入(不需要传入signature和timestamp)
# 具体有哪些参数请参考帮助中心: "https://help.kuaidaili.com/api/getdps/"
# 返回ip列表
# 注意：若您使用的是python2, 且在终端调用，或在文件中调用且没有加 "# -*- coding: utf-8 -*-" 的话
# 传入area参数时，请传入unicode类型，如 area=u'北京,上海'
ips = client.get_dps(2, sign_type='hmacsha1', format='json', pt=2, area='北京,上海,广东')
print("dps proxy: ", ips)


# 检测私密代理有效性： 返回 ip: true/false 组成的dict
ips = client.get_dps(2, sign_type='simple', format='json')
valids = client.check_dps_valid(ips)
print("valids: ", valids)


# 获取计数版ip余额（仅私密代理计数版）
balance = client.get_ip_balance(sign_type='hmacsha1')
print("balance: ", balance)


