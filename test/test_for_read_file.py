# -*- coding:UTF-8 -*-
'''
Created on 2017-9-17

@author: Administrator
'''
from tools.get_text import read_file
from tools.myprint import *
from hcj.caijing_hangye import *
from tools.To_Mysql import ToMysql
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
obj = read_file()
# pretty_list(obj)
url = obj[1]['source_url']
name = obj[1]['source_name']
print url
ans= caijing_hangye(url,name)
# ans =[{
#             'title':"title",
#             'author':"news_source",
#             'time':now,
#             'source':"name",#sina finance
#             'type':'1',
#             'keywords':"keywords",
#             'viewer':'0',
#             'score':'0',     
#             'content':u"發垃圾分類登記法"   
#         }]
# cur = ToMysql()
# cur.insert_list(ans)
# cur.commit()
# pretty_list(ans)

# for i in obj:
#     url = i['source_url']
#     sina_finance(url)
