#!/usr/bin/python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: DeleteURL.py
# Author: yuhaitao
# mail: acer_yuhaitao@163.com
# Created Time: Tue 04 Apr 2017 08:22:00 PM PDT
#########################################################################
import re
import shutil
import os
import sys 
import re
import cgi,cgitb
import codecs


#接收数据
#def RecvFromForm():
form = cgi.FieldStorage()
getName = form.getvalue('deletenetName')
getURL = form.getvalue('deletenetURL')
getPaswd = form.getvalue('deletepwd')
#将gb2312转换成utf-8
strRecv = getName.decode("gb2312").encode("utf-8")


#读取文件
#print file('d:\\a.txt').read()
str = strRecv + "</a></li>"
tt = [str]
SAVEURL  = "My Test!"

#打开文件删除指定内容所在行
def DeleteURL():
	filewrite = open('/home/pi/github/FindNetURL.txt','w')
    
        with open('/www/right.html','r') as f:
		with open ('/home/pi/righttmp.html','w') as g:
			for line in f.readlines():
				if all(string not in line for string in tt) :
					g.write(line)
				else :
                                        try :
					    filewrite.write(line)
	            			    filewrite.close()
                                        except IOError:
                                            print "IOError"
        
        shutil.move('/home/pi/righttmp.html','/www/right.html')
        #os.rename('/www/righttmp.html','/www/right.html')

def SucessPrin():

	fileread = open('/home/pi/github/FindNetURL.txt','r')
	SAVEURL = fileread.readline()
	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>"
	print "<meta http-equiv=\"Content-Type\"content=\"text/html;charset=utf-8\"/>"
	print "<title>远程添加网址测试实例</title>"
	print "</head>"
	print "<body>"
	print "<h2>网站名称:%s </h2>" %	(strRecv)
	print "<h2>网站地址:%s </h2>" % (SAVEURL)
	print "<h2><font color=\"#FF0000\" size=\"+3\">提交成功！</font>本页面3秒后自动关闭.</h2>"
	print "<meta http-equiv=\"refresh\" content=\"3; url=../HT-Test.html\">"
	print "<script type=\"text/jscript\">"
	print "setTimeout(\"self.close()\",3000)"
	print "</script>"
	print "</body>"
	print "</html>"
	fileread.close()
	fileremove = "/home/pi/github/FindNetURL.txt"
	if os.path.exists(fileremove) :
		os.remove(fileremove)
	else :
		FaildPrin()
def FaildPrin():
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
	print "<h2><font color=\"#FF0000\" size=\"+3\">提交失败！</font>本页面3秒后自动关闭.</h2>"
	print "<meta http-equiv=\"refresh\" content=\"3; url=../HT-Test.html\">"
	print "<script type=\"text/jscript\">"
	print "setTimeout(\"self.close()\",3000)"
	print "</script>"
	print "</body>"
	print "</html>"

if getPaswd == "haitao":
        if ((getName != "") or (getURL != "")):
	#if getName != "" :
		DeleteURL()
		SucessPrin()
	else :
		FaildPrin()
else :
	FaildPrin()

