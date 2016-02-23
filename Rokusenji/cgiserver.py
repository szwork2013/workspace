#! /usr/local/bin/python
# coding: utf-8

import CGIHTTPServer,SimpleHTTPServer,BaseHTTPServer


server_address = (u"", 8002)
handler_class = CGIHTTPServer.CGIHTTPRequestHandler #1 ハンドラを設定
server = BaseHTTPServer.HTTPServer(server_address, handler_class)
server.serve_forever()

"""
import CGIHTTPServer
import SocketServer

PORT=8002
Handler=CGIHTTPServer.CGIHTTPRequestHandler
httpd=SocketServer.TCPServer(("",PORT),Handler)

print "serving at port",PORT
httpd.serve_forever()
"""