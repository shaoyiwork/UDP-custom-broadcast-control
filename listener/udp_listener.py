#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import * 
from time import sleep
import os

#UDP listener init
PORT = 9999
s = socket(AF_INET,SOCK_DGRAM)  

s.bind(('',PORT))
print '...waiting for message..'

while True: # Run forever
    data,address = s.recvfrom(1024)
    print data,address
    if data == "start" :
        sleep(1) # Sleep for 1 second
        os.system('sudo python your_python.py')
	print 'OK start to do cmd'

