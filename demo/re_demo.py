import datetime
import re



print(re.findall('\\d+','a3bc'))
# E20180209075001141753024
# E20180511102031102691373
text="E20180209075001141753024 E20180209075001141753024E20180511102031102691370 E201805111020311026913722 E20180511102031102691373 E20180211102031102691370 退回到公司需要寄回；充电不正常"

m = re.findall(r"E201\d{20}",text)

print(m)
print(datetime.datetime.now())

if m:
    print(m[0])
else:
    print('not match')



print('========')
print('========')
dict = {'Name': 'Zara', 'Age': 7}

print('========')


line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj2.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

print('========')

line2 = "2018/08/16-23:36:46.534 INFO [kafka-consumer-prod-order-4-thread-1] com.babyfs.service.user.impl.UserCourseServiceImpl:397>>send promoter order push service msg userId:1651246, orderId:190418"


matchObj = re.findall(r'(\d{4}/\d{2}/\d{2}-\d{2}:\d{2}:\d{2}.\d{3}) (.*?):(.*?):',
                              line2)
print(matchObj.pop()[2])

exit(0)
print('========')


aaa='2018/08/15-08:20:54.127 WARN [kafka-consumer-prod-order-4-thread-1] com.babyfs.service.order.impl.YzOrderItemServiceImpl:141>>后台未配置的code编码:0305200008,msg：未找到数据,queryCode'
# line2=aaa
matchObj2 = re.findall(r'INFO .* com.babyfs.service.yz.impl.YzAPIServiceImpl:326>>trade info resp :(.*?)', line2)
print(line2)
print(matchObj2)
print(type(matchObj2[0]))
print(type(matchObj2[0]))
print(type(matchObj2))

t=list(matchObj2.pop())
print(list(t))
print(list(t)[0])
print(list(t)[1])
# print(list(matchObj2[0]))


aaa='2018/08/15-08:20:54.127 WARN [kafka-consumer-prod-order-4-thread-1] com.babyfs.service.order.impl.YzOrderItemServiceImpl:141>>后台未配置的code编码:0305200008,msg：未找到数据,queryCode'




