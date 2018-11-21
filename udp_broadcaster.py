#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
 
HOST = '<broadcast>'
PORT = 9999
BUFSIZE = 1024
 
ADDR = (HOST, PORT)
udpCliSock = socket(AF_INET, SOCK_DGRAM)
udpCliSock.bind(('', 0))
udpCliSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    data = raw_input('please input cmd >')
    if not data:
        break
    print "broadcast sending -> %s"%data
    udpCliSock.sendto(data,ADDR)

udpCliSock.close()
