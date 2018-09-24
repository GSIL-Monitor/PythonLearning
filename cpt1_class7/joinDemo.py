import datetime

t1 = datetime.datetime.now()

sp = ''
for i in range(100000000):
    a = sp + 'sxt'

t2 = datetime.datetime.now()

print(t2.timestamp()-t1.timestamp())
print(t1)
print(t2)


t3 = datetime.datetime.now()
sp = ''
li=[]
for i in range(100000000):
    li.append('sxt')
sp.join(li)

t4 = datetime.datetime.now()
print(t4.timestamp() - t3.timestamp())
print(t3)
print(t4)
