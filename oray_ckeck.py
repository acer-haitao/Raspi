#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re

while(1) :
    var = os.popen("sudo phddns  status | grep ONLINE | sed -n \"1,0p\"").read()
    #print  var.split(":")
    #list = re.match(r'Runstatus:  ONLINE',var)
    #print list
    #str = list.group()
    #print str
    if ('|              Runstatus:  ONLINE                   |\n' == var) :
        print "花生壳客户端已经登录成功"
        os.system("sleep 30")
    else :
        print "正在重启花生壳客户端"
        os.system("yes | sudo phddns stop")
        os.system("sleep 10")
        os.system("sudo phddns start")
        os.system("sleep 90")

