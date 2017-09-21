# -*- coding:UTF-8 -*-
'''
Created on 2017-9-21

@author: Administrator
'''
import MySQLdb

# 打开数据库连接
class ToMysql():  
    def __init__(self):    
        try:  
            self.db = MySQLdb.connect("121.42.186.86","root","123456","hcj" )       
            # 使用cursor()方法获取操作游标 
            self.cur = self.db.cursor()
            self.cur.execute("set names utf8")
            # 使用execute方法执行SQL语句
            self.cur.execute("SELECT VERSION()")      
            # 使用 fetchone() 方法获取一条数据库。
            data = self.cur.fetchone()  
            print "Database version : %s " % data
        except MySQLdb.Error as e:  
            print("Mysql Error %d: %s" % (e.args[0], e.args[1])) 
    def query(self,sql):  
        try:  
            self.cur.execute("set names utf8")
            n=self.cur.execute(sql)  
            print 'here'
            print n
            return n  
        except MySQLdb.Error as e:  
            print("Mysql Error:%s\nSQL:%s" %(e,sql))  
  
    def queryRow(self,sql):  
        self.query(sql)  
        result = self.cur.fetchone()  
        return result  
  
    def queryAll(self,sql):  
        self.query(sql)  
        result=self.cur.fetchall()  
        desc =self.cur.description  
        d = []  
        for inv in result:  
            _d = {}  
            for i in range(0,len(inv)):  
                _d[desc[i][0]] = str(inv[i])  
            d.append(_d)  
        return d  
    def qu_chong(self,p_data,p_table_name =u'hcj'):
        print p_data
        tpye = p_data['type']
        title = p_data['title']
        content = p_data['content']
        sql_for_qu_chong = u''
        if(tpye=='1'):
            sql_for_qu_chong = u"SELECT id FROM "+p_table_name+u" WHERE content = '"+content+u"'"
        else:
            sql_for_qu_chong = u"SELECT id FROM "+p_table_name+u" WHERE title = '"+title+u"'"
        print sql_for_qu_chong
        result = self.queryRow(sql_for_qu_chong)
        if(result):
            return False
        else:
            return True

    def insert(self,p_data,p_table_name =u'hcj'): 
        if (self.qu_chong(p_data, p_table_name)):
            for key in p_data:  
                p_data[key] = u"'"+str(p_data[key])+u"'"  
            key   = ','.join(p_data.keys())  
            value = ','.join(p_data.values())  
            real_sql = u"INSERT INTO " + p_table_name + u" (" + key + u") VALUES (" + value + u")"  
            #self.query("set names 'utf8'")  
            print real_sql
            return "insert result\t"+str(self.query(real_sql)) 
        else:
            return "Already exits"
    def insert_list(self,p_data,p_table_name ='hcj'): 
        for item in p_data:
            print self.insert(item, p_table_name)
    def getLastInsertId(self):  
        return self.cur.lastrowid  
  
    def rowcount(self):  
        return self.cur.rowcount  
  
    def commit(self):  
        self.conn.commit()  
  
    def __del__(self):
        '''free source.'''
        try:
            self.cur.close()
            self.con.close()
        except:
            pass

    def close(self):
        self.__del__()