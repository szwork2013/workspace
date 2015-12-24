#! /Users/yuta/.pyenv/shims/python3
# coding: utf-8
import http.server

server_address = ("", 8002)
handler_class = http.server.CGIHTTPRequestHandler #1 ハンドラを設定
server = http.server.HTTPServer(server_address, handler_class)
server.serve_forever()
