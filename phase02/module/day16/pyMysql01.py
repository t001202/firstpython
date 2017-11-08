#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "WangYx"
import pymysql

connect = pymysql.Connect(host="localhost",
                          user="root",
                          password="123456",
                          database="test",
                          port=3306,
                          charset='utf8')
cursor = connect.cursor()

sql = "SELECT * FROM unit_hobby"
cursor.execute(sql)
for params in cursor.fetchall():
	print(params[1])
print("共查找出: " + str(cursor.rowcount) + "条数据")
