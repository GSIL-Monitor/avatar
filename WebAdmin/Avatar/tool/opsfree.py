# -*- coding: utf-8 -*- 
'''
Created on 2011-6-21
@author: yaofang.zjl
1. 定时任务一天跑一次
2. 先将opshosts记录清空，再追加写入一次
3. 在写入的同时依据名称变更关联表中的数量
'''
import json
import MySQLdb
import urllib
ops_hostgroup_list = "http://opsfree.corp.taobao.com:9999/nodes.json?_username=droid/droid&e=1&n=0&q=manifest==nodegroup"
url_handle=urllib.urlopen(ops_hostgroup_list)
data = json.loads(url_handle.read())
conn = MySQLdb.connect(db='avatar',host='10.13.114.23', user='admin',passwd='123456',charset='utf8') 
cursor = conn.cursor()  
cursor.execute("delete from opshosts")
conn.commit()  
for ele in data:
    nodegroup_name = ele.get('nodegroup_name')
    nodegroup_id = ele.get('_id')
    url = "http://opsfree.corp.taobao.com:9999/nodes.json?_username=droid/droid&e=1&n=0&q=nodegroup==%s"%(nodegroup_name)
    u_handle=urllib.urlopen(url)
    try:
        u_data = json.loads(u_handle.read())
        nodegroup_num = len(u_data)
    except Exception,e:
        print nodegroup_name
        nodegroup_num = 0
    insert_sql = "insert into `opshosts` (`hostgroup` ,`hostnumber`,`hostgroupid`) values ('%s',%d,%d)" %(nodegroup_name,int(nodegroup_num),int(nodegroup_id))
    cursor.execute(insert_sql)
    """2.变量关联表<名称与数量>"""
    update_sql = "update snapserver set `hostgroup`='%s',hostnumber=%d where hostgroupid=%d"%(nodegroup_name,int(nodegroup_num),int(nodegroup_id))
    cursor.execute(update_sql)
conn.commit()  
cursor = None
conn = None