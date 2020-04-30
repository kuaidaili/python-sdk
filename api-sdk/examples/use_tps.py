# -*- coding: utf-8 -*-

"""隧道代理使用示例
   接口鉴权说明：
   目前支持的鉴权方式有 "simple" 和 "hmacsha1" 两种，默认使用 "simple"鉴权。
   所有方法均可添加关键字参数sign_type修改鉴权方式。
"""

import kdl
auth = kdl.Auth("test_order_id","test_api_key")
client = kdl.Client(auth)

expire_time = client.get_order_expire_time()
print("expire time:",expire_time)

# 获取ip白名单, 返回ip列表
ip_whitelist = client.get_ip_whitelist()
print("ip whitelist:", ip_whitelist)

# 设置ip白名单，参数类型为字符串或列表或元组
# 成功则返回True, 否则抛出异常
client.set_ip_whitelist([])
client.set_ip_whitelist("171.113.244.40")
print(client.get_ip_whitelist())

# 显示隧道代理当前的ip
ip = client.tps_current_ip()
print("current_ip:",ip)


# 改变当前隧道ip
new_ip = client.change_tps_ip()
print("new_ip:",new_ip)

# 获取代理鉴权信息
# 获取指定订单访问代理IP的鉴权信息。
# 鉴权信息包含用户名密码，用于请求私密代理/独享代理/隧道代理时进行身份验证。
# plain_text 为1 表示明文显示用户名和密码
# 具体请看：https://www.kuaidaili.com/doc/api/getproxyauthorization/
proxyauthorization = client.get_proxy_authorization(plain_text=1,sign_type='simple')
print("proxyauthorization: ", proxyauthorization)

# 获取隧道代理IP
# 获取订单对应的隧道代理IP。
# 具体参数请查看：https://www.kuaidaili.com/doc/api/gettps/
proxy_list = client.get_tps_ip(2,sign_type='hmacsha1', format='json')
print(proxy_list)




