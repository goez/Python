#!/usr/bin/env python

# server.py
# simple python server
# receives content and prints to the screen

import socket
s = socket.socket()
host = 'localhost'
port = 13337
s.bind((host,port))

s.listen(5)
while True:
  c,addr = s.accept()
  print 'Got connection from ',addr
  c.send('Pyhton socket server')
  c.close()
