# -*- coding: utf-8 -*- 

import json
import MySQLdb
import urllib
ops_hostgroup_list = "http://opsfree.corp.taobao.com:9999/nodes.json?_username=droid/droid&e=1&n=0&q=manifest==nodegroup"
url_handle=urllib.urlopen(ops_hostgroup_list)
data = json.loads(url_handle.read())
print len(data)


#import commands,re
#file = "/home/avtar/zjl/a/algoyt1.kgb.cnz.alimama.com"
#cmd = 'sed -n \'/###END OF AVATAR###/,$p\' ' + file+'|sed -e 1d';
#tmp=commands.getstatusoutput(cmd)
##print tmp[1]
#
#tmpa = commands.getstatusoutput("sed -n '/diff_files=/p' /home/avtar/zjl/a/algoyt1.kgb.cnz.alimama.com|awk -F '=' '{print $2}'")[1].replace('\"','')
##print tmpa
#
#def txt_wrap_by(start_str, end, html):
#    start = html.find(start_str)
#    if start >= 0:
#        start += len(start_str)
#        end = html.find(end, start)
#        if end >= 0:
#            return html[start:end].strip()
#
#
#            
#
##title = re.findall("<title.*?\/title>", fds)
#
##d={}
##/home/a/share/phoenix/algo_db/hadoop/bidword/conf/push_data.conf.diff
##/home/a/share/algo1/spendsmooth/setting/conf/camPlan.conf.diff
##
#import sys
#d={}
#totalcontent  = tmp[1]          #后面的解析数据来源于这个字符串的内容
##
#tmpaa = tmpa.split()
##
#k=0
#for i, v in enumerate(tmpaa):
##    print i,v
#    if len(tmpaa[i+1:i+2]) == 0:
#        #The End of list
#        t= tmpaa[i:i+1][0]
#        start_index=totalcontent.find(t)
##        print totalcontent[start_index:].strip()
##        name = tmpaa[i:i+1][0].split("/")[-1]
##        cmdend = "sed -n '/###END OF AVATAR###/,$p' /home/avtar/zjl/a/algoyt1.kgb.cnz.alimama.com |sed -e 1d|sed -n '/%s/,$p'|sed -e '$d'" % (name)
##        print cmdend
#    else:
#        f = tmpaa[i:i+1][0].strip()
#        if f=="/home/a/share/algo1/xprofile/UserIntentionBuyClick/script/buyconvert.sh.diff":
#            print "==="*9
#            t = tmpaa[i+1:i+2][0]
#            start_index = totalcontent.find(f)
#            if start_index>-1:
#                end_index = totalcontent.find(t,start_index)
#                print totalcontent[start_index:end_index].strip()
#                print "---------------------------------------------------------------------\n\n\n"
#            else:
#                print "*"*100
#        
#        
##        print txt_wrap_by(f,t,totalcontent)
##        print f
##        print t
#        
#        
##        cmdend = "sed -n '/###END OF AVATAR###/,$p' /home/avtar/zjl/a/algoyt1.kgb.cnz.alimama.com |sed -e 1d|sed -n '/%s/,/%s/p'|sed -e '$d'" % (f,t)
##        print cmdend
#    
##    vv = commands.getstatusoutput(cmdend)[1].replace('\"','')
##    
##    d[i] = vv
##    
#    
#    
##
##
##""""""
##base_rpms_num = commands.getstatusoutput("sed -n '/base_rpms_num=/p' /home/click_package|awk -F '=' '{print $2}'")
##num = base_rpms_num[1]
##print num
##base_rpm_list = commands.getstatusoutput("sed -n '/base_rpms=/p' /home/click_package|awk -F '=' '{print $2}'")
##mys = base_rpm_list[1].replace('\"','')
##
#
#
##sed -n '/###END OF AVATAR###/,$p' /home/click_package |sed -e 1d|sed -n '/tsar_alert.conf.diff/,$p'|sed -e '$d'
##
##a= mys.split()
##a.sort()
###print "\n".join(a)
##
##
##tmpa = commands.getstatusoutput("sed -n '/diff_files=/p' /home/click_package|awk -F '=' '{print $2}'")[1].replace('\"','')
##
###print tmpa.split()
#
#
#
#"""
#sed -n '/base_rpms_num=/p' /home/click_package|awk -F '=' '{print $2}'     获取base_rpms_num的值
#"""
#
#"""
#sed -n '/base_rpms=/p' /home/click_package|awk -F '=' '{print $2}'     获取base_rpms的值
#"""
#
#"""
#sed -n '/cust_rpms=/p' /home/click_package|awk -F '=' '{print $2}'     获取base_rpms的值
#"""
#
#"""
#sed -n '/cust_rpms_num=/p' /home/click_package|awk -F '=' '{print $2}'      获取base_rpms的值
#"""
#
##sed -n '/diff_files=/p' /home/click_package|awk -F '=' '{print $2}' 