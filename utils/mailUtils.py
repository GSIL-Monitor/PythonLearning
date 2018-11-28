import json
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def mail_send(mail_body='', send_from='wangchenchen@babyfs.cn', send_to='wangchenchen@babyfs.cn'):
    mb_json = json.loads(mail_body)
    title = '[{type}] {event} {time}'.format(type=mb_json['type'],
                                             event=mb_json['event'],
                                             time=datetime.datetime.now())
    mail_host = "smtp.qiye.163.com"  # 设置服务器
    # mail_user = "wangchenchen@babyfs.cn" #用send_from
    mail_pass = "Shasky2017"  # 口令
    mail_msg = '{data}'.format(data=mb_json['data'])

    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header(send_from)
    message['To'] = Header(send_to)
    message['Subject'] = Header(title, 'utf-8')

    try:
        print(send_from, send_to)
        print(message.as_string())
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(send_from, mail_pass)
        smtpObj.sendmail(send_from, send_to, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    json_data = {'type': 'name1', 'event': '18', 'data': {'url': 'urlsssss', 'user_name': 'sssname'}}
    post_data = json.dumps(json_data)
    mail_send(mail_body=post_data, send_to='wangchenchen@babyfs.cn')
