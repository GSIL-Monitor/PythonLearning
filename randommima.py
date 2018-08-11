# -*- coding:utf-8 -*-  
from functools import reduce
import random,string
a_length=9
mima = random.sample(string.ascii_letters + string.digits, a_length)
mimaout = reduce( (lambda x, y: x + y ), mima)
print(mima)
print(mimaout)
print(''.join(mima))

import time,datetime
print(time.strftime( "%Y%m%d %H:%M:%S", time.localtime()))

# print(time.time())
# print(datetime.time())
# print(datetime.strptime('%Y%m%d %H:%M:%S %f',datetime.time())


