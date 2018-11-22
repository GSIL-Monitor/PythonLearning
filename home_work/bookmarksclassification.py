import datetime
import re

def tug(**kwargs):
    # 对输入参数分词


    # 找出关键词，分级别


    # 返回带级别的关键词
    # eg: Apache.Hive
    return ''
    pass


bookmarksfile = '/Users/admin/Documents/bookmarks_2018_11_22.html'

with open(bookmarksfile) as reader:
    kv = {}
    i=0
    for line in reader:
        pattern1 = re.compile(r'<DT><A HREF="(.*?)" ADD_DATE="(.*?)">(.*?)</A>', re.M|re.I|re.S)
        pattern2 = re.compile(r'<DT><A HREF="(.*?)" ADD_DATE="(.*?)" ICON="(.*?)">(.*?)</A>', re.M|re.I|re.S)
        if pattern2.findall(line):
            # 4
            match = pattern2.findall(line)
            url = match[0][0]
            add_date = match[0][1]
            title = match[0][3]
            ICON = match[0][2]
        elif pattern1.findall(line):
            match = pattern1.findall(line)
            url = match[0][0]
            add_date = match[0][1]
            title = match[0][2]
            ICON = None
        else:
            match=url= add_date= title =None
            pass

        if match:
            # tug = ''
            i=i+1
            kv[url] = title
            # print(i,url,add_date,title)
            # print(match)
    print(kv)