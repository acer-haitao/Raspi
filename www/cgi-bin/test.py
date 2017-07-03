#!/usr/bin/python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: addreplace.py
# Author: yuhaitao
# mail: acer_yuhaitao@163.com
# Created Time: Fri 31 Mar 2017 07:05:13 PM PDT
#########################################################################
import os
import sys 
import re
import cgi,cgitb
import codecs
import time
import pymysql
#接收数据
def RecvFromForm():
    db = pymysql.connect("127.0.0.1","root","haitao","mynetdb" )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO mynet(Num,Name,URL)VALUES (1,"Test","12345")"""
    try:
     # 执行sql语句
        cursor.execute(sql)
    # 提交到数据库执行
        db.commit()
    except:
    # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
        db.close()
#替换字符串中的addURL和addName，并将替换后的结果写入文件中
RecvFromForm()
