#!/bin/python3

import socket

ls = socket.socket()
port = 9011
max_connect = 2
ip = socket.gethostname()
ls.bind((ip, port))
ls.listen(max_connect)
print(f"server started at {ip} on port {port}")
clientsocket, address = ls.accept()

while True:
      msg = clientsocket.recv(1024).decode()
      print (msg)
