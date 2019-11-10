#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# C:\Users\win 10\AppData\Local\Programs\Python\Python37

# manual operation mysql databases;
# command : show databases;
# CREATE DATABASE test;
# use test;
# show tables;
# CREATE TABLE table_name (column_name column_type);    #column_type:https://www.runoob.com/mysql/mysql-data-types.html
# describe table_test;
# INSERT INTO table_name ( field1, field2,...fieldN ) VALUES ( value1, value2,...valueN );
# select * from table_test;
    # INSERT INTO runoob_tbl  (runoob_title, runoob_author, submission_date) VALUES  ("python", "one day", NOW());
# 创建一个表格：name 性别 出生年月日
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)