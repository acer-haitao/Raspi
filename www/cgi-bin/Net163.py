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
form = cgi.FieldStorage()
#getURL = form.getvalue('netURL')
#接受xmlhttp.open("GET","/cgi-bin/SqltoHtml.py?q="+str,true)传递的参数
getNum = form.getvalue('q')


def DbSongName(song_id,cursor):
    sql_song_name = """SELECT * FROM  music163 WHERE song_id = %s """ %(song_id)
    #sql_song_name = """SELECT * FROM  music163 WHERE song_id=186016;"""
    #print sql_song_name
    try:
        cursor.execute(sql_song_name)
        results = cursor.fetchall()
        for row in results:
            name = row[2]
    except Exception , e:
        print "DbSong"+str(e)
        db.rollback()
        db.close()
    return name

def Dbinsert():
    PrintTable()
    db = MySQLdb.connect("bdm273925510.my3w.com","bdm273925510","haitao131","bdm273925510_db",charset='utf8' )
    cursor = db.cursor()
    sql ="""SELECT * FROM  comment163 WHERE liked  > %s order by liked DESC """ %(getNum)
    #sql ="""SELECT * FROM  comment163 WHERE liked  > %s order by liked DESC """ % (500000)
    #sql ="""SELECT * FROM  comment163 WHERE liked  > 500000 order by liked DESC """
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
	for i, row in enumerate(results):
	    id = row[0]
	    song_id = row[1]
            #print song_id 
            song_name = DbSongName(song_id,cursor).encode('UTF-8')
            #print song_name
	    txt = row[2]
	    author = row[3]
            liked = row[4]
            txtcv = txt.encode('UTF-8')
            authorcv = author.encode('UTF-8')
            form1 = '''
                    <table class="table">
                        <tr>
                            <td>
                            <button type="button" class="btn-default btn-lg btn-block">
                                <blockquote class="blockquote-reverse">
                                <p class="text-left lead" >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s</p>
                                <footer> <cite title="Source
                                Title">序号:%s--歌名:%s--评论数:%s--%s</cite></footer>
                                </blockquote>
                        </button>
                        </td>
                        </tr>
                    </table>
                    ''' 
            print form1 % (txtcv,i,song_name,liked,authorcv)
        print "</body>"
        print "</html>"
    except Exception , e:
        print "Dbinsert"+str(e)
        db.rollback()
        db.close()
def PrintTable():
    print "Content-type:text/html"
    print
    print "<html>"
    print "<head>"
    print "<meta http-equiv=\"Content-Type\"content=\"text/html;charset=utf-8\"/>"
    print "<title>远程添加网址测试实例</title>"
    print "<link rel=\"stylesheet\" href=\"https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css\" crossorigin=\"anonymous\">"    
Dbinsert()
