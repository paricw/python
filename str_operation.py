#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# C:\Users\win 10\AppData\Local\Programs\Python\Python37


# 普通字符串的基本操作

import re
 
#str_list = "[11.23,23.34]"
#list_list = ast.literal_eval(str_list)
test_str =  "wc phone 15608018049 "

# print (test_str.replace("wc","zsw"))  # 局限性：只适用于这一个字符串
# print (test_str.strip())







# 正则表达式，更通用的一种解析字符串的一种方法
#search,match,compile
#需要字符串是否含有 “phone”
# if (re.search("ed",test_str) != None):
    # print("find")
# else:
    # print("not find")


s = '1102231990xxxxxxxx'
#\d{3}  \d匹配一个数字字符  有3个数字组成的一个字符串"123"  "s34"
#?      
res = re.search('(?P<province>\d{3})',s) #pattern 的含义要弄清楚
print(res.groupdict())
