# -*- coding: utf-8 -*-

"""独享代理使用示例
   接口鉴权说明：
   目前支持的鉴权方式有 "simple" 和 "hmacsha1" 两种，默认使用 "simple"鉴权。
   所有方法均可添加关键字参数sign_type修改鉴权方式。
"""

import kdl

auth = kdl.Auth("test_order_id", "test_api_key")
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

# 提取独享代理ip, 第一个参数为提取的数量, 其他参数以关键字参数的形式传入(不需要传入signature和timestamp)
# 具体有哪些参数请参考帮助中心: "https://www.kuaidaili.com/doc/api/getdps/"
# 返回ip列表
# 注意：若您使用的是python2, 且在终端调用，或在文件中调用且没有加 "# -*- coding: utf-8 -*-" 的话
# 传入area参数时，请传入unicode类型，如 area=u'北京,上海'
ips = client.get_kps(2, sign_type='hmacsha1', format='json', pt=2, area='北京,上海,广东')
print("kps proxy: ", ips)
