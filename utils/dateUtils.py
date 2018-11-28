# -*- encoding: utf-8 -*-
import datetime, time
from functools import wraps


def dayAdd(ds, i, fmt='%Y%m%d'):
    """
    :param ds:传入日期字符串,格式为'%Y%m%d'
    :param i:要增加的天数,减少输入负数
    :return ds:返回增加天数后的日期,格式为'%Y%m%d'=yyyymmdd
    """
    # 其他的时间增减的方式
    # date = date + datetime.timedelta(days=-1) 天
    # date + datetime.timedelta(hours=-1) 时
    # date + datetime.timedelta(minutes=-1) 分
    # date + datetime.timedelta(seconds=-1) 秒
    return (datetime.datetime.strptime(ds, fmt) + datetime.timedelta(days=-i)).strftime(fmt)


def today(fmt='%Y%m%d'):
    """
    :param fmt: 默认格式为'%Y%m%d'=yyyymmdd,可选参数
    :return: 当天日期时间字符串
    """
    return datetime.datetime.today().strftime(fmt)


def yesterday(fmt='%Y%m%d'):
    """
    :param fmt: 默认格式为'%Y%m%d'=yyyymmdd,可选参数
    :return: 昨天日期时间字符串
    """
    return (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime(fmt)


def yestermonth(fmt='%Y%m'):
    return datetime.datetime.now().replace(month=datetime.datetime.now().month - 1).strftime(fmt)


def firstdayofmonth(fmt='%Y%m%d'):
    return datetime.datetime.strptime(datetime.datetime.now().strftime('%Y%m'), '%Y%m').strftime(fmt)


def endtimeofyestermonth():
    return str(
        datetime.datetime.strptime(datetime.datetime.now().strftime('%Y%m'), '%Y%m') + datetime.timedelta(seconds=-1)
    )


def float2str(start, fmt='%Y-%m-%d %H:%M:%S.%f'):
    return datetime.datetime.fromtimestamp(start).strftime(fmt)


def run_time(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = wrapper.__name__
        start = datetime.datetime.now()
        print('{now} {func} run begin.'.format(now=start, func=func_name))
        func(*args, **kwargs)
        end = datetime.datetime.now()
        cost = end.timestamp() - start.timestamp()
        print('{now} {func} run end.cost time:{cost} s'.format(now=end, func=func_name, cost=cost))

    return wrapper


if __name__ == '__main__':
    @run_time
    def ss(n):
        print('sleep {n} seconds.'.format(n=n))
        time.sleep(n)


    ss(2)

    # print(yesterday())
    # print(firstdayofmonth())
    # print((endtimeofyestermonth()))
    # print(yestermonth())
