# -*- coding: utf-8 -*-
import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

user = '249398363@qq.com'
Mailbox = poplib.POP3_SSL('pop.qq.com', '995')
Mailbox.user(user)
#QQ邮箱第三方客户端采用授权码登陆
Mailbox.pass_('nfqogpzxhiqrbiag')


print('Messages: %s. Size: %s' % Mailbox.stat())
resp, mails, octets = Mailbox.list()
numMessages = len(mails) #  邮件总数
print(numMessages)
# list()返回所有邮件的编号:
# 可以查看返回的列表类似['1 82923', '2 2184', ...]
print(mails)

# 遍历收件箱
msg=[]
for i in range(3):
    for e_mail in Mailbox.retr(i+1)[1]:
        # 打印邮件
        print(Parser().parsestr(e_mail))
        msg.append(email)

# 退出
print(msg.__len__())

Mailbox.quit()
