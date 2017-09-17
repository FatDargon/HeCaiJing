# -*- coding:UTF-8 -*-
'''
Created on 2017-9-17

@author: Administrator
'''
str = '''
【宋晓梧谈老工业基地改造：要以民生为出发点和落脚点】原国务院振兴东北办副主任宋晓梧17日在淄博
'''

import re
aa=  re.search('【.+】', str).group()
aa = re.sub('[【】]', '', aa)
print aa