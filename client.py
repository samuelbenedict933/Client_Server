#!/bin/python3

import socket
s = socket.socket()
hostname =  socket.gethostname()
port = 9011
#you can choose any port
s.connect((hostname, port))

while True:
      x = input("enter message:")
      s.send(x.encode())
