



import time
import datetime
print(datetime.datetime.now())


t = time.time()

print (t)                       #原始时间数据
print (int(t))                  #秒级时间戳
print (int(round(t * 1000)))    #毫秒级时间戳

nowTime = lambda:int(round(t * 1000))
print (nowTime());              #毫秒级时间戳，基于lambda

print(datetime.datetime.now())
print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   #日期格式化




###### 秒数转字符串
ts = 1515774430
dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
print(dt)

###### 秒数转time
print( time.localtime(ts) )

###### 毫秒数转字符串
st=1505923200000
dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(st)/1000.0))
print(dt)


