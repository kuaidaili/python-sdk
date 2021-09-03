#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import ssl
import websocket


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_open(ws):
    data = '{}'  # 此处填入您需要传给目标网站的json格式参数，如{"type":"web","data":{"_id":"xxxx"}}
    ws.send(data)


def on_close(*args):
    print("### closed ###")


proxies = {
    "http_proxy_host": "59.38.241.25",
    "http_proxy_port": 23916,
    "http_proxy_auth": ("username", "password"),
}


def start():
    websocket.enableTrace(True)
    target_url = 'ws://127.0.0.1:5000/socket.io/?EIO=4&transport=websocket'  # 此处替换您的目标网站
    ws = websocket.WebSocketApp(
        url = target_url,
        header = [
            "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
        ],
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE}, **proxies)


if __name__ == "__main__":
    start()
