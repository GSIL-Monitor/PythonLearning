# -*- encoding: gb2312 -*-
import email

with open('傲游面试邀请（收到请回复）.eml', "r") as fp:
    msg = email.message_from_file(fp)

    subject = msg.get("subject")  # 取信件头里的subject,　也就是主题
    # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC?=这样的subject
    h = email.Header.Header(subject)
    dh = email.Header.decode_header(h)
    subject = dh[0][0]
    print("subject:", subject)
    print("from: ", email.utils.parseaddr(msg.get("from"))[1])  # 取from
    print("to: ", email.utils.parseaddr(msg.get("to"))[1])  # 取to

# 循环信件中的每一个mime的数据块
for par in msg.walk():
    if not par.is_multipart():
        name = par.get_param("name")
        if name:
            #有附件,输出附件名字
            h = email.Header.Header(name)
            dh = email.Header.decode_header(h)
            fname = dh[0][0]
            print('附件名:', fname)

            # data = par.get_payload(decode=True)  # 解码出附件数据，然后存储到文件中
            # try:
            #     f = open(fname, 'wb')  # 注意一定要用wb来打开文件，因为附件一般都是二进制文件
            # except:
            #     print '附件名有非法字符，自动换一个'
            # f = open('aaaa', 'wb')
            # f.write(data)
            # f.close()
        else:
            #输出,邮件正文
            print(par.get_payload(decode=True))  # 解码出文本内容，直接输出来就可以了。

    print('+' * 60)  # 用来区别各个部分的输出
