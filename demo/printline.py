import time
import datetime
print("跑程序",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

input_file = "/Users/admin/logstash-2.4.1/sample/input.txt"

f = open(input_file, 'a')

a = 0
while a < 1000:
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write('\nhello boy! ' +t )
    a += 1
    time.sleep(1)
    print(t)

f.close()

f = open(input_file, 'r')
print(f.read())
f.close()
