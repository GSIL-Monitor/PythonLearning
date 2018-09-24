import re

def getTime(time_file):
    ss = open(time_file).read()

    timelist = re.findall('\d\d:\d\d', ss)

    # print(ss)
    # print(timelist)

    tt = 0.0
    for time1 in timelist:
        tmin = int(time1.split(':')[0])
        tsec = int(time1.split(':')[1])
        tt = tmin + tt + tsec / 60.0

        # print(time1)

    print(tt)

if __name__ == '__main__':
    time_file = ['time.txt','time2.txt']
    for time_f in time_file:
        getTime(time_f)
    pass
