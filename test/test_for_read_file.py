# -*- coding:UTF-8 -*-
'''
Created on 2017-9-17

@author: Administrator
'''
from tools.get_text import read_file
from tools.myprint import *
from hcj.sina_finance import *

obj = read_file()
# pretty_list(obj)
url = obj[0]['source_url']
print url
pretty_list(sina_finance(url))

# for i in obj:
#     url = i['source_url']
#     sina_finance(url)
