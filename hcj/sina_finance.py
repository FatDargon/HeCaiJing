# -*- coding:UTF-8 -*-
'''
Created on 2017-9-17

@author: Administrator
'''
from tools.GetSoup import *
from dateutil import parser
import re
url = 'https://live.sina.com.cn/zt/f/v/finance/globalnews1'
def sina_finance(url):
    big_data=[]
    soup = Soup(url,'utf-8').get_soup()
    news_list = soup.find_all(attrs={"data-nick":'fin_图文直播'},limit=100)
    for news in news_list:
#         print news.get_text(strip = True)
        time_str = news.find('p',class_='bd_i_time_c').get_text(strip = True)
        datetime_struct = parser.parse(time_str)
        time = datetime_struct.strftime('%Y-%m-%d %H:%M:%S')
#         print 'time \t'+datetime_struct.strftime('%Y-%m-%d %H:%M:%S') # 2016-12-22 13:58:59
        content =  news.find('div',class_='bd_i_txt').get_text(strip = True)
#         re_title =re.compile()
#         print content
        try:
            news_source_tmp = re.search(u'（.+）', content).group()
            news_source =re.sub(u'[（）]', '', news_source_tmp)
#             print 'news_source\t'+news_source
            content = re.sub(u'（.+）','',content)
        except:
#             print 'news_source\tnone'
            news_source = ''
        try:
            title_tmp = re.search(u'【.+】', content).group()
            title = re.sub(u'[【】]', '', title_tmp)
#             print 'title\t'+title
            text = re.sub(title_tmp, '', content)
#             print 'text\t'+text
        except:
            title = ''
            text = content
#             print "title\tnone"
#             print 'title\t'+content
        small_data = {
            'title':title,
            'author':news_source,
            'time':time,
            'source':'sina finance',#sina finance
            'type':'',
            'keywords':'',
            'view':'',
            'score':'',     
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
            'view':'',
            'score':'',
            'content':''   
        }
    return big_data