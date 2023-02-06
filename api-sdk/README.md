# 简介
快代理api SDK

# 依赖环境
1. python2.7 到 python3.7
2. 从[快代理](https://www.kuaidaili.com)购买相应产品
3. [获取订单的`secret_id`和`secret_key`](https://www.kuaidaili.com/usercenter/api/secret/)

# 获取安装
安装 Python SDK 前，请先获取订单对应的`secret_id`和`secret_key`，请严格保管，避免泄露。

## 通过pip安装(推荐)
您可以通过`pip`将SDK安装到您的项目中：
```
pip install kdl
```

如果您的项目环境尚未安装`pip`，可参考：
* Ubuntu/Debian安装pip：`apt-get install python-setuptools`
* CentOS安装pip：`yum install python-setuptools`
* MacOS安装pip: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; python get-pip.py`

您还可以参考[pip官网](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o)进行安装。

## 通过源码包安装
前往 [Github 代码托管地址](https://github.com/kuaidaili/python-sdk/tree/master/api-sdk) 下载最新代码，解压后

```
$ cd api-sdk
$ python setup.py install
```

## 示例
以私密代理订单使用为例
``` python
# -*- coding: utf-8 -*-

"""私密代理使用示例
   接口鉴权说明：
   目前支持的鉴权方式有 "token" 和 "hmacsha1" 两种，默认使用 "token"鉴权。
   所有方法均可添加关键字参数sign_type修改鉴权方式。
"""

import kdl

auth = kdl.Auth("secret_id", "secret_key")
client = kdl.Client(auth, timeout=(8, 12), max_retries=3)

# 获取订单到期时间, 返回时间字符串
expire_time = client.get_order_expire_time()
print("expire time", expire_time)



# 获取ip白名单, 返回ip列表
ip_whitelist = client.get_ip_whitelist()
print("ip whitelist", ip_whitelist)

# 设置ip白名单，参数类型为字符串或列表或元组
# 成功则返回True, 否则抛出异常
client.set_ip_whitelist([])
client.set_ip_whitelist("171.113.244.40,171.113.244.41")
print(client.get_ip_whitelist())



client.set_ip_whitelist(tuple())

# 提取私密代理ip, 第一个参数为提取的数量, 其他参数以关键字参数的形式传入(不需要传入signature和timestamp)
# 具体有哪些参数请参考帮助中心: "https://www.kuaidaili.com/doc/api/getdps/"
# 返回ip列表
# 注意：若您使用的是python2, 且在终端调用，或在文件中调用且没有加 "# -*- coding: utf-8 -*-" 的话
# 传入area参数时，请传入unicode类型，如 area=u'北京,上海'
ips = client.get_dps(2, sign_type='hmacsha1', format='json', pt=2, area='北京,上海,广东')
print("dps proxy: ", ips)


# 检测私密代理有效性： 返回 ip: true/false 组成的dict
ips = client.get_dps(2, sign_type='simple', format='json')
valids = client.check_dps_valid(ips)
print("valids: ", valids)

# 获取私密代理剩余时间: 返回 ip: seconds(剩余秒数) 组成的dict
ips = client.get_dps(5, format='json')
seconds = client.get_dps_valid_time(ips)
print("seconds: ", seconds)


# 获取计数版ip余额（仅私密代理计数版）
balance = client.get_ip_balance(sign_type='hmacsha1')
print("balance: ", balance)

# 获取代理鉴权信息
# 获取指定订单访问代理IP的鉴权信息。
# 鉴权信息包含用户名密码，用于请求私密代理/独享代理/隧道代理时进行身份验证。
# plain_text 为1 表示明文显示用户名和密码
# 具体请看：https://www.kuaidaili.com/doc/api/getproxyauthorization/
proxyauthorization = client.get_proxy_authorization(plain_text=1,sign_type='simple')
print("proxyauthorization: ", proxyauthorization)
```
您可以在examples目录下找到更详细的示例

## 参考资料

* [查看API列表](https://www.kuaidaili.com/doc/api/)
* [了解API鉴权](https://www.kuaidaili.com/doc/api/auth/)
