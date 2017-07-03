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
#def RecvFromForm():
form = cgi.FieldStorage()
getURL = form.getvalue('netURL')
getName = form.getvalue('netName')
getAddNum = form.getvalue('addnumber')
getPaswd = form.getvalue('pwd')
#将gb2312转换成utf-8
strRecv = getName.decode("gb2312").encode("utf-8")
#操作数据库create table mynet(Num int(5),Name varchar(100),URL varchar(200))character set uft8;
def Dbinsert():
    Strtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    db = pymysql.connect("127.0.0.1","root","haitao","mynetdb",charset='utf8')
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO mynet(Num,Name,URL,Time) VALUES (%s,%s,%s,%s) """
    try:
    # 执行sql语句
        cursor.execute(sql,[getAddNum,strRecv,getURL,Strtime])
    # 提交到数据库执行
        db.commit()
    except:
    # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
        db.close()
#替换字符串中的addURL和addName，并将替换后的结果写入文件中
def ReplaceStr():
	str = "<li><a href=\"addURL\" target=\"_blank\">addName</a></li>\n"
	getURLstr = str.replace("addURL",getURL)
	getLast = getURLstr.replace("addName",strRecv)

	file = open("/home/pi/github/addneturl.txt","w")
	file.write(getLast)
	file.close()

#读取文件中的字符串写入到另一个文件
def AddStrToFile():
	file = open("/www/right.html", "r")
	fileadd = open("/home/pi/github/addneturl.txt", "r")
	content = file.read()
	contentadd = fileadd.read()
	file.close()
	fileadd.close()

	pos = content.find("<!--add%s-->"%(getAddNum))
	if pos != -1 :
		content =  content[:pos] + contentadd + content[pos:]
		file = open("/www/right.html","w")
		file.write(content)
		file.close()
#提交成功响应
def SucessPrin():
	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>"
	print "<meta http-equiv=\"Content-Type\"content=\"text/html;charset=utf-8\"/>"
	print "<title>远程添加网址测试实例</title>"
	print "</head>"
	print "<body>"
	print "<h2>网站名称:%s </h2>" %	(strRecv)
	print "<h2>网站地址:%s </h2>" % (getURL)
	print "<h2><font color=\"#FF0000\"	size=\"+3\">提交成功！</font>本页面3秒后自动关闭.</h2>"
        print "<meta http-equiv=\"refresh\" content=\"3; url=../HT-Test.html\">"
	print "<script type=\"text/jscript\">"
	print "setTimeout(\"self.close()\", 3000)"
	print "</script>"
	print "</body>"
	print "</html>"
        SaveLog(strRecv, getURL)
#提交失败响应
def FaildPrin():
	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>"
	print "<meta charset=\"utf-8\">"
	print "<title>远程添加网址测试实例</title>"
	print "</head>"
	print "<body>"
	print "<h2>网站名称:%s </h2>" %	(strRecv)
	print "<h2>网站地址:%s </h2>" % (getURL)
	print "<h2><font color=\"#FF0000\"size=\"+3\">本提交失败！请检查您的输入是否有误!该页面3秒后自动关闭</font></h2>"
        print "<meta http-equiv=\"refresh\" content=\"3\";   url=../HT-Test.html\">"
	print "<script type=\"text/jscript\">"
	print "setTimeout(\"self.close()\", 3000)"
	print "</script>"
	print "</body>"
	print "</html>"
def SaveLog(strRecv, getURL) :
    Strtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    try :
        LogFile = open("/home/pi/github/Add_Del_NetLog.txt","a+")
        LogFile.write("\n+++++++++++++++++++++++++++++++++++++++++\n")
        LogFile.write("时间:" + Strtime + "-->添加网站:\n")
        LogFile.write("网站名称:" + strRecv + "\n")
        LogFile.write("网站地址:" + getURL + "\n")
        LogFile.close()
    except IOError:
        LogFile.close()

if getPaswd == "haitaoadd" :
        Dbinsert()
        ReplaceStr()
	AddStrToFile()
	SucessPrin()
else :
	FaildPrin()





