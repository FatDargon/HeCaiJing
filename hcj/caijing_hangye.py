# -*- coding:utf-8 -*-  
'''
Created on 2017年9月27日

@author: Administrator
'''
# -*- coding:UTF-8 -*-
'''
Created on 2017-9-17

@author: Administrator
'''
from tools.GetSoup import *
from dateutil import parser
import re
import jieba
import jieba.posseg
import jieba.analyse
from tools.Get_html import *

def caijing_hangye(url,name):
    name = name.decode('utf-8')
    big_data=[]
#     soup=get_html(url,3,True,True)
    soup = Soup(url,'').get_soup()
#     print soup
    news_list = soup.find('div',class_='main_lt').ul.find_all('li',limit = 2)
    for news in news_list:
        try:
            title = news.div.a.get_text(strip = True)
            new_url = news.div.a['href']        
        except:
            title = ''
            new_url = ''
        author = news.find('div',class_='author').get_text(strip = True)   
        new_soup = get_html(new_url,0,False,True)
#         new_soup = Soup(url,'').get_soup()
#         print new_soup
#         exit()
        text = new_soup.find('div', id='the_content').get_text(strip = True)
        try:
            kw_str = new_soup.find('div',class_='ar_keywords').find_all('a')
            keywords = ''
            for i in kw_str:
                keywords = keywords+'/'+i.get_text(strip = True)
        except:
            keywords = ''
        try:
            time_str = new_soup.find('span',id='pubtime_baidu').get_text(strip = True)
            datetime_struct = parser.parse(time_str)
            time = datetime_struct.strftime('%Y-%m-%d %H:%M:%S')
        except:
            now = datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S")
            time = now
        small_data = {
            'title':title,
            'author':author,
            'time':time,
            'source':name,#sina finance
            'type':'1',
            'keywords':keywords[1:],
            'viewer':'0',
            'score':'0',     
            'content':text   
        }
        big_data.append(small_data) 
        small_data={
            'title':'',
            'author':'',
            'time':'',
            'source':'',#sina finance
            'type':'',
            'keywords':'',
            'viewer':'',
            'score':'',
            'content':''   
        }
    return big_data