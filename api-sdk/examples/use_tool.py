import sys

from kdl.client import Client
from kdl.auth import Auth

auth = Auth("test_order_id", "test_api_key")
client = Client(auth)

# 提取User Agent 第一个参数为提取的数量, 其他参数以关键字参数的形式传入(不需要传入signature和timestamp)
# 具体有哪些参数请参考帮助中心: "https://www.kuaidaili.com/doc/api/getua/"
# 返回user agent列表
ua = client.get_ua(10, browser="weixin")
print("ua:", ua)