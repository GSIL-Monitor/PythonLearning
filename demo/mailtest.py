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


mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
<!-- Row Highlight Javascript -->
window.onload=function(){
 var tfrow = document.getElementById('tfhover').rows.length;
 var tbRow=[];
 for (var i=1;i<tfrow;i++) {
 tbRow[i]=document.getElementById('tfhover').rows[i];
 tbRow[i].onmouseover = function(){
 this.style.backgroundColor = '#ffffff';
 };
 tbRow[i].onmouseout = function() {
 this.style.backgroundColor = '#bedda7';
 };
 }
};
<style type="text/css">
table.tftable {font-size:12px;color:#333333;width:100%;border-width: 1px;border-color: #9dcc7a;border-collapse: collapse;}
table.tftable th {font-size:12px;background-color:#abd28e;border-width: 1px;padding: 8px;border-style: solid;border-color: #9dcc7a;text-align:left;}
table.tftable tr {background-color:#bedda7;}
table.tftable td {font-size:12px;border-width: 1px;padding: 8px;border-style: solid;border-color: #9dcc7a;}
</style>

<table id="tfhover" class="tftable" border="1">
<tr><th>Header 1</th><th>Header 2</th><th>Header 3</th><th>Header 4</th><th>Header 5</th></tr>
<tr><td>Row:1 Cell:1</td><td>Row:1 Cell:2</td><td>Row:1 Cell:3</td><td>Row:1 Cell:4</td><td>Row:1 Cell:5</td></tr>
<tr><td>Row:2 Cell:1</td><td>Row:2 Cell:2</td><td>Row:2 Cell:3</td><td>Row:2 Cell:4</td><td>Row:2 Cell:5</td></tr>
<tr><td>Row:3 Cell:1</td><td>Row:3 Cell:2</td><td>Row:3 Cell:3</td><td>Row:3 Cell:4</td><td>Row:3 Cell:5</td></tr>
<tr><td>Row:4 Cell:1</td><td>Row:4 Cell:2</td><td>Row:4 Cell:3</td><td>Row:4 Cell:4</td><td>Row:4 Cell:5</td></tr>
<tr><td>Row:5 Cell:1</td><td>Row:5 Cell:2</td><td>Row:5 Cell:3</td><td>Row:5 Cell:4</td><td>Row:5 Cell:5</td></tr>
<tr><td>Row:6 Cell:1</td><td>Row:6 Cell:2</td><td>Row:6 Cell:3</td><td>Row:6 Cell:4</td><td>Row:6 Cell:5</td></tr>
</table>

"""

message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header(send_from)
message['To'] = Header(','.join(send_to))

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(send_from, send_to, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")