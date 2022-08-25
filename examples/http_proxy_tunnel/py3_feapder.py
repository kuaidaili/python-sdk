import feapder


class Py3Feapder(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://dev.kdlapi.com/testproxy")

    def download_midware(self, request):
        # 隧道域名:端口号
        tunnel = "XXX.kdlapi.com:15818"

        # 用户名密码认证
        username = "username"
        password = "password"
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
        }

        # 白名单认证(需提前设置白名单)
        # proxies = {
        #     "http": "http://%(proxy)s/" % {"proxy": tunnel},
        #     "https": "http://%(proxy)s/" % {"proxy": tunnel}
        # }

        request.proxies = proxies
        return request

    def parse(self, request, response):
        print(response.text)


if __name__ == "__main__":
    Py3Feapder().start()
