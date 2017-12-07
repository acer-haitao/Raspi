#!/usr/bin/python
#-*- coding: utf-8 -*-
#########################################################################
# Author: yuhaitao
# mail: acer_yuhaitao@163.com
# Created Time: Tue 10 Jan 2017 04:23:30 AM PST
#########################################################################
import cgi
import pymysql
import codecs

def PrintTable():
    print  "Content-type:text/html"
    print
    print  "<html>"
    print  "<head>"
    print  "<meta http-equiv=\"Content-Type\"content=\"text/html;charset=utf-8\"/>"
    print  "<title>王者荣耀英雄皮肤图片收集</title>"
    print  "</head>"
    print  "<body>"
    print  "<h1 align=\"center\">王者荣耀英雄皮肤图片收集</h1>"

def DbSELECTALIYUN():
    PrintTable()
    try:
        db = pymysql.connect("bdm273925510.my3w.com","bdm273925510","haitao131","bdm273925510_db",charset='utf8')
    except Exception as e:
        print ("数据库连接失败",e)

    # 使用cursor()方法获取操作游标
    try:
        cursor = db.cursor()
    except Exception:
        print("获取操作游标异常",Exception)

    sql = """select *from WZRY"""
    try:
    # 执行sql语句
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                num = row[0]
                id = row[1].encode('UTF-8')
                name = row[2].encode('UTF-8')
                skinname = row[3].encode('UTF-8')
                skinurl = row[4].encode('UTF-8')
                time = row[5].encode('UTF-8')
                src = """<a href=\"%s\"><img src=\"%s\" alt=\"%s\"       
                class=\"post-image\" width=\"auto\" height=\"500\" /></a>""" % (skinurl,skinurl,name)
                print  "<div class=\"panel\" style=\"width:auto;text-align:center\">"
                print  "<div class=\"subfeature\">"
                print (src)
                print  "</div>"
                print  "</div>"
                print  "<h2 align=\"center\">%s  %s</h2>" % (name,skinname)
            print  "</body>"
            print  "</html>"
        except Exception as e:
            print ("执行SQL语句异常:",e)
    # 提交到数据库执
        db.commit()
    except Exception as e:
    # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
        db.close()
        print  ("发生异常:",e)
DbSELECTALIYUN()
