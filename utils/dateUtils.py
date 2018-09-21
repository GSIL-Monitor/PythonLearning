# utf-8


def day_add(ds, i):
    # 传入日期和要增加的天数,返回增加天数后的日期
    # 日期限定格式:yyyymmdd
    import datetime
    return (datetime.datetime.strptime(ds, '%Y%m%d') + datetime.timedelta(days=-i)).strftime('%Y%m%d')


# date = datetime.datetime.strptime(ds,'%Y%m%d')
# date = date + datetime.timedelta(days=-1)
# date + datetime.timedelta(hours=-1)
# date + datetime.timedelta(minutes=-1)
# date + datetime.timedelta(seconds=-1)
