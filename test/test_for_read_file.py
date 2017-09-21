# -*- coding:UTF-8 -*-
'''
Created on 2017-9-17

@author: Administrator
'''
from tools.get_text import read_file
from tools.myprint import *
from hcj.sina_finance import *
from tools.To_Mysql import ToMysql
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
obj = read_file()
# pretty_list(obj)
url = obj[0]['source_url']
name = obj[0]['source_name']
print url
# ans= sina_finance(url,name)
ans =[{
            'title':"title",
            'author':"news_source",
            'time':now,
            'source':"name",#sina finance
            'type':'1',
            'keywords':"keywords",
            'view':'0',
            'score':'0',     
            'content':u"阿三收到尽快发货是肯定就发贺卡健身房"   
        }]
cur = ToMysql()
cur.insert_list(ans)
# pretty_list(ans)

# for i in obj:
#     url = i['source_url']
#     sina_finance(url)
