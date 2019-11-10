#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# C:\Users\win 10\AppData\Local\Programs\Python\Python37

def dict_base():
    # 基本概率：1.字典 2.可查询对应的K-V 3.

    # 描述小王，小张，小成的成绩为 1， 22 ，0
    student ={"xiaowang":1,'xiaozhang':22,'xiaocheng':0}

    # for k in student:
        # print (k,':',student[k])
        
    # 新增 小美 成绩为 100
    # student.append('xiaomei':100) erro
    student["xiaomei"] = 100

    # 如何判断是否有 小思的成绩？
    # 思路1：循环判断有没有小思
    print('xiaosi' in student)
    # print(student['xiaosi'])
    print('xiaowang' in student)
    # 描述小王(312015)，小张(312016)，小成(312017)的成绩为 1， 22 ，0

    # Student = {"xiaowang":(312015,1),'xiaozhang':(312016,22),'xiaocheng':(312017,0)}
    # Student = {"xiaowang":{"number":312015,"score":1},'xiaozhang':{"number":312016,"score":22},'xiaocheng':{"number":312017,"score":0}}

    # for k in Student:
        ### print (k,':',Student[k][0])
        # print (k,':',Student[k]["number"])


  
# list 

#1.集合 2.可改 
# 防止越界
def list_base():
    Num = [1,2,3,4,5]
    Num.append(6)     #Num是一个list类型的数据，list有 append 与 pop 方法。
    # for i in Num:
        # print (i)
    prn_obj(Num)
    
    # Num.pop(1)
    # for i in Num:
        # print (i)

# test_dict_list = {"xiaowang":[1,2,3,4,5],'xiaozhang':22,'xiaocheng':0}
    # test_dict_list["xiaomei"][1]   #test_dict_list["xiaomei"] = [1,2,3,4,5]
                                   # test_dict_list["xiaomei"][0] = 1



