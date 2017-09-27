# -*- coding:utf-8 -*-  
'''
Created on 2017年9月27日

@author: Administrator
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","","hcj" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "insert into hcj (content) values ('aaa')"
try:
   # 执行SQL语句
   cursor.execute(sql)
   db.commit()
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()