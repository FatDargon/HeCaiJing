# -*- coding:utf-8 -*-  
'''
Created on 2017年9月27日

@author: Administrator
'''
from tools.get_text import read_file
from tools.myprint import *
from hcj.sina_finance import *
from tools.To_Mysql import ToMysql
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
obj = read_file()
from tools.Get_SQL import *

ans ={
            'title':"title",
            'author':"news_source",
            'time':now,
            'source':"name",#sina finance
            'type':'1',
            'keywords':"keywords",
            'view':'0',
            'score':'0',     
            'content':"阿三收到尽快发货是肯定就发贺卡健身房"   
}
print get_s_sql('hcj', ['id'], {'content':'阿三收到尽快发货是肯定就发贺卡健身房'}, 0)