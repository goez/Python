#!/usr/bin/env python

# client program
# Found on http://www.securitytube.net/video/1933

import socket

s = socket.socket()
host = 'localhost'
port = 13337
s.connect((host,port))
print s.recv(1024)
s.close
