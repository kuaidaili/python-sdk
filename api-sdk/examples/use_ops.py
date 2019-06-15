# -*- coding: utf-8 -*-

"""
    开放代理使用示例
    接口鉴权说明：
    目前支持的鉴权方式有 "simple" 和 "hmacsha1" 两种，默认使用 "simple"鉴权。
    所有方法均可添加关键字参数sign_type修改鉴权方式。
"""

import kdl

auth = kdl.Auth("yourorderid", "yourapikey")
client = kdl.Client(auth)

# 获取订单到期时间, 返回时间字符串
expire_time = client.get_order_expire_time()
print("expire time", expire_time)


# 提取开放代理ip, 第一个参数为提取的数量, 其他参数以关键字参数的形式传入(不需要传入signature和timestamp)
# 具体有哪些参数请参考帮助中心: "https://help.kuaidaili.com/api/getdps/"
# 返回ip列表
# 注意：若您使用的是python2, 且在终端调用，或在文件中调用且没有加 "# -*- coding: utf-8 -*-" 的话
# 传入area参数时，请传入unicode类型，如 area=u'北京,上海'
# 若您是开放代理svip订单，请传入order_level='svip', 若您是开放代理专业版订单，请传入order_level='ent'
ips = client.get_proxy(2, sign_type='hmacsha1', order_level='svip', format='json', pt=2, area='北京,上海,广东')
print("ops proxy: ", ips)


# 检测开放代理有效性
ips = client.get_proxy(2, sign_type='hmacsha1', order_level='svip', format='json', pt=2, area='北京,上海,广东')
valids = client.check_ops_valid(ips)
print("valids: ", valids)
