import feapder


class Py3Feapder(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://dev.kdlapi.com/testproxy")

    def download_midware(self, request):
        # 提取代理API接口，获取1个代理IP
        api_url = "http://dps.kdlapi.com/api/getdps/?secret_id=o1fjh1re9o28876h7c08&signature=xxxxx&num=1&pt=1&sep=1"

        # 获取API接口返回的代理IP
        proxy_ip = feapder.Request(api_url).get_response().text

        # 用户名密码认证(私密代理/独享代理)
        username = "username"
        password = "password"
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
        }

        # 白名单认证(需提前设置白名单)
        # proxies = {
        #     "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
        #     "https": "http://%(proxy)s/" % {"proxy": proxy_ip}
        # }

        request.proxies = proxies
        return request

    def parse(self, request, response):
        print(response.text)


if __name__ == "__main__":
    Py3Feapder().start()
