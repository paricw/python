#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import mysql.connector
#
#
# con = mysql.connector.connect(host='localhost', user="root", passwd="123456")
#
# #print(con)
#
import mysql.connector

#create a interface which connected local datebase
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM runoob_tbl")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)
