# -*- coding:UTF-8 -*-
'''
Created on 2017-9-17

@author: Administrator
'''
from tools.get_text import read_file
from tools.myprint import *

obj = read_file()
# pretty_list(obj)
url = obj[0]['source_url']
print url