# -*- coding:UTF-8 -*-
'''
Created on 2017-9-17

@author: Administrator
'''
from tools.get_text import read_file
from tools.myprint import *
import time

ISOTIMEFORMAT='%Y-%m-%d %X'
obj = read_file()
# pretty_list(obj)
for item in obj:
    source_name = item['source_name']
    source_url = item['source_url']
    if('新浪财经实时直播' in source_name):
        print time.strftime(ISOTIMEFORMAT, time.localtime( time.time() ) )\
        +"\tin the: "+source_name
    else:
        print "no"
        break