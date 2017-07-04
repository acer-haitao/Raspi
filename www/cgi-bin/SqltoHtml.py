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
import MySQLdb
#接收数据
#def RecvFromForm():
#form = cgi.FieldStorage()
#getURL = form.getvalue('netURL')
#getName = form.getvalue('netName')
#getAddNum = form.getvalue('addnumber')
#getPaswd = form.getvalue('pwd')
#将gb2312转换成utf-8
#strRecv = getName.decode("gb2312").encode("utf-8")
#操作数据库create table mynet(Num int(5),Name varchar(100),URL varchar(200))character set uft8;
def Dbinsert():
    PrintTable()
    db = MySQLdb.connect("127.0.0.1","root","haitao","mynetdb",charset='utf8' )
    #db = MySQLdb.connect("127.0.0.1","root","haitao","mynetdb")
    # print "mysql"
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 查询语句
    #sql = """INSERT INTO mynet(Num,Name,URL,Time) VALUES (%s,%s,%s,%s) """
    sql ="""SELECT * FROM mynet WHERE Num = 10 """
    try:
    # 执行sql语句
        # print "try"
        cursor.execute(sql)
        #print "tryafter"
        results = cursor.fetchall()
        #print results;
	for row in results:
	    Num = row[0]
	    Name = row[1]
	    URL = row[2]
	    Time = row[3]
            Nameconver = Name.encode('UTF-8')
            #print Nameconver
            print "<tr>"
            print "<td>%s</td>" % (Num)
            print "<td>%s</td>" % (Nameconver)
            print "<td>%s</td>" % (URL)
            print "<td>%s</td>" % (Time)
            print "</tr>"
	    #print "Num = %s Name = %s URL = %s Time = %s" % (Num,Name,URL,Time) 
        print "</table>"
        print "</body>"
        print "</html>"
    except:
    # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
        db.close()
#替换字符串中的addURL和addName，并将替换后的结果写入文件中
def PrintTable():
        print "Content-type:text/html"
        print
        print "<html>"
        print "<head>"
        print "<meta http-equiv=\"Content-Type\"content=\"text/html;charset=utf-8\"/>"
        print "<title>远程添加网址测试实例</title>"
        print "</head>"
        print "<body>"
        print "<table border='1' width='80%' align='center'>"
	print "<tr>"
	print "<th>编号</th>"
	print "<th>网站名称</th>"
	print "<th>网站地址</th>"
	print "<th>添加时间</th>"
	print "</tr>"

Dbinsert()
