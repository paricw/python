#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# C:\Users\win 10\AppData\Local\Programs\Python\Python37

import sys
import socket

client_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = socket.gethostbyname(socket.gethostname())
#print(Host)
Port = 8223
BUFSIZ = 1024

client_soc.connect((Host, Port))

while True:
    #终端输入函数，一直阻塞，直到有输入返回
    data1 = input('>')
    #data = str(data)

    client_soc.send(data1.encode('utf-8'))
    print("send", data1.encode('utf-8'))
    #阻塞等待数据接收
    data1 = client_soc.recv(BUFSIZ)
    print("recv", data1)
    # break
client_soc.close()
