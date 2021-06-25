#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用HTTP代理发送websocket请求
"""
import gzip
import zlib

import websocket

OPCODE_DATA = (websocket.ABNF.OPCODE_TEXT, websocket.ABNF.OPCODE_BINARY)

url = "ws://echo.websocket.org/"

proxies = {
    "http_proxy_host": "59.38.241.25",
    "http_proxy_port": 23916,
    "http_proxy_auth": ("username", "password"),
}

ws = websocket.create_connection(url, **proxies)


def recv():
    try:
        frame = ws.recv_frame()
    except websocket.WebSocketException:
        return websocket.ABNF.OPCODE_CLOSE, None
    if not frame:
        raise websocket.WebSocketException("Not a valid frame %s" % frame)
    elif frame.opcode in OPCODE_DATA:
        return frame.opcode, frame.data
    elif frame.opcode == websocket.ABNF.OPCODE_CLOSE:
        ws.send_close()
        return frame.opcode, None
    elif frame.opcode == websocket.ABNF.OPCODE_PING:
        ws.pong(frame.data)
        return frame.opcode, frame.data

    return frame.opcode, frame.data


def recv_ws():
    opcode, data = recv()
    if opcode == websocket.ABNF.OPCODE_CLOSE:
        return
    if opcode == websocket.ABNF.OPCODE_TEXT and isinstance(data, bytes):
        data = str(data, "utf-8")
    if isinstance(data, bytes) and len(data) > 2 and data[:2] == b'\037\213':  # gzip magick
        try:
            data = "[gzip] " + str(gzip.decompress(data), "utf-8")
        except Exception:
            pass
    elif isinstance(data, bytes):
        try:
            data = "[zlib] " + str(zlib.decompress(data, -zlib.MAX_WBITS), "utf-8")
        except Exception:
            pass
    if isinstance(data, bytes):
        data = repr(data)

    print("< " + data)


def main():
    print("Press Ctrl+C to quit")
    while True:
        message = input("> ")
        ws.send(message)
        recv_ws()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nbye')
    except Exception as e:
        print(e)