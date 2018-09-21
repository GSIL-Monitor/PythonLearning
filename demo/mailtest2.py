# -*- coding: utf-8 -*-
import datetime
import sys

ds = sys.argv[0]

print("avgrlen="+str(len(sys.argv)),";ds="+str(ds),";datetime="+str(datetime.datetime.now()))

import smtplib
from email.mime.text import MIMEText
from email.header import Header

send_from = 'wangchenchen@babyfs.cn'
send_to = ['wangchenchen@babyfs.cn']  # 接收邮件
# ,'wangzhaoshen@babyfs.cn'

# 第三方 SMTP 服务
mail_host="smtp.qiye.163.com"  #设置服务器
mail_user="wangchenchen@babyfs.cn"    #用户名
mail_pass="Shasky2017"   #口令


mail_msg = "======  massage  ======"

message = MIMEText(mail_msg, 'html')
message['From'] = Header(send_from)
message['To'] = Header(','.join(send_to))

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(send_from, send_to, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")


import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header


# 第三方 SMTP 服务
mail_host="smtp.qiye.163.com"  #设置服务器
mail_user="wangchenchen@babyfs.cn"    #用户名
mail_pass="Shasky2017"   #口令

receivers = "wangchenchen@babyfs.cn"
message = MIMEText("使用加密的SMTP协议测试下邮件吧", 'plain', 'utf-8')
subject = u'SMTP WITH SSL'
message['Subject'] = Header(subject, 'utf-8')
smtpObj = SMTP_SSL(mail_host)
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(mail_user,  receivers, message.as_string())
print ("邮件发送成功")
