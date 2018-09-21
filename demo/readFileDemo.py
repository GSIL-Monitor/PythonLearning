import datetime
import re
import json


def get_keywords(file_path):
    file_obj = open(file_path, 'rU')
    keyword_count = {}
    for LINE in file_obj:
        match_obj = re.findall(r'\d{4}/\d{2}/\d{2}-\d{2}:\d{2}:\d{2}.\d{3} (.*?):(.*?):',
                               LINE)
        if len(match_obj) != 0:
            t1 = match_obj.pop()
            l1 = ':'.join(list(t1))
            if keyword_count.get(l1) is None:
                keyword_count[l1] = 1
            else:
                keyword_count[l1] = 1 + keyword_count[l1]
        else:
            print(LINE)

    print(keyword_count)
    pass


file = ['/Users/admin/Documents/工作文件夹/项目/商城/有赞商城数据/app.2018-08-15.log',
        '/Users/admin/Documents/工作文件夹/项目/商城/有赞商城数据/app.2018-08-16.log']

# getKeyWords(file[0])

print(file)

file_object = open(file[0], 'rU')
# print(len(file_object))
# 1534346898071
# 1505923200000
try:
    for line in file_object:
        matchObj = re.findall(
            r'(\d{4}/\d{2}/\d{2}-\d{2}:\d{2}:\d{2}.\d{3}) .* com.babyfs.service.yz.impl.YzAPIServiceImpl:326>>trade info resp : (\{.*\})',
            line)
        if len(matchObj) != 0:
            print('=======≥≤≠–“‘æ……∆˙√ç∂ΩßΩåœ™¡™£¢∞§¶•ªªªªººº–‘“ø¥†®∑œåß∂ƒ©˙∆˚¬æ…æ≥≤µ∫√ç≈ΩΩ=====')
            time_order = matchObj.pop()
            ct_1 = datetime.datetime.strptime(time_order[0], '%Y/%m/%d-%H:%M:%S.%f')
            ct = int(ct_1.timestamp() * 1000)
            log = time_order[1]
            print(time_order[0], ct_1, ct)
            print(log)
            # order_json = json.loads(matchObj[0])
            # print(order_json.get('response').keys())
            # print(order_json.get('response').get('order_promotion').keys())
            # refund_order = order_json.get('response').get('refund_order')
            #
            # # if len(refund_order)!=0:
            # #     print(line)
            # #     print(refund_order)
            #
            # print(order_json.get('response').get('full_order_info').keys())

finally:
    file_object.close()
