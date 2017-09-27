# -*- coding:utf-8 -*-  
'''
Created on 2017年9月27日

@author: Administrator
'''
import MySQLdb
from tools.get_text import read_file
from tools.myprint import *
from hcj.sina_finance import *
from tools.To_Mysql import ToMysql
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
obj = read_file()
db = MySQLdb.connect("localhost","root","","hcj")       
            # 使用cursor()方法获取操作游标 
cur =db.cursor()
cur.execute("set names utf8")
            # 使用execute方法执行SQL语句
cur.execute("SELECT VERSION()")      
            # 使用 fetchone() 方法获取一条数据库。
data = cur.fetchone()  
print "Database version : %s " % data
ans ={
            'title':"title",
            'author':"news_source",
            'time':now,
            'source':"name",#sina finance
            'type':'1',
            'keywords':"keywords",
            'viewer':'0',
            'score':'0',     
            'content':"ASD"   
        }
sql = "INSERT INTO `hcj` (`type`) VALUES ('1')"
sql1 = "SELECT `id` FROM `hcj`"
try:  
    print sql.decode('utf-8')
    cur.execute("set names utf8")
    n=cur.execute(sql.decode('utf-8'))  
    print n
    result = cur.fetchall()
    for r in result:
        print r[0]
except MySQLdb.Error as e:  
    print("Mysql Error:%s\nSQL:%s" %(e,sql)) 