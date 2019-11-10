#!/usr/bin/env python3
# -*- coding: utf-8 -*-


file_name = "dict_list.py"
# file_object = open(file_name, 'w+')  #文件操作模式 'r' 'w' 'r+' 'w+' 'a'
# file_object.write("hello world!")
# file_object.close()

file_read = open(file_name, 'r', encoding='gb18030', errors='ignore')
while True:
    read_str = file_read.readline()
    print(read_str)
    if len(read_str) == 0:
        break
file_read.close()
