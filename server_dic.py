#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# C:\Users\win 10\AppData\Local\Programs\Python\Python37
#grade_table[3333]
import re
import sys
import socket

#将其·更改为一个数据库类
#属性:grade_table
#方法:查询成绩，创建服务(tcp_server)


grade_table = {3333:(78,79,80),4444:(48,49,50),5555:(98,98,98),6666:(77,78,79),7777:(87,100,87)
}
print(grade_table)

server_dic = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建tcp socket+
Host = socket.gethostbyname(socket.gethostname())
#print(Host)
Port = 8223
BUFSIZ = 1024

server_dic.bind((Host,Port))
#让socket 进入监听模式（监听socket）
server_dic.listen(5)

while True:
    print('waiting for connection...')
    #一直阻塞，当client 连接时，会返回连接socket 与 client 的ip地址+
    client_socket, client_addr = server_dic.accept()          
    print(client_socket,client_addr)
    
    while True:
        #通过连接socket，接收客户端发来的数据，会返回接收到的数据
        #当客户端连接时断开时，会返回 0
        data = client_socket.recv(BUFSIZ)  
        if len(data) == 0:                       #识别客户端断开的情况
            break
        print("recv",data)
        Deal_d = str(data.decode('utf-8'))
        # 前4个字符必须为数字
        if (re.search("\d{4}",Deal_d) != None):     # 前4位必须是数字  
            if (re.search("\+",Deal_d) != None):    # 输入学号\+0（3333+0）
                name=int(Deal_d[0:4])
                kemu=int(Deal_d[-1])
                #key 是否存在
                if name in grade_table:
                    client_socket.send(str(grade_table[name][kemu]).encode('utf-8'))
                else:
                    client_socket.send(("name is not in the database error").encode('utf-8')) 
            else :  #  输入学号(3333) 
                name=int(Deal_d[0:4])
                #key 是否存在
                if name in grade_table:
                    client_socket.send(str(grade_table[name]).encode('utf-8'))
                else:
                    client_socket.send(("name is not in the database error").encode('utf-8')) 
        else :
            client_socket.send(("input error").encode('utf-8')) #输入 sss9dd
    client_socket.close()
server_dic.close()