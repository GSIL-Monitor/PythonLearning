import datetime

file = '/Users/admin/Downloads/sqlresult_3197931.csv'
open_file = open(file, 'r')
write_count = 0
for r in open_file:
    # print(r)
    name = r.split(',')[1].strip().strip('"')
    mobile = r.split(',')[0].strip('"')
    # print(name, mobile)
    f = open("/Users/admin/Downloads/out/{name}.csv".format(name=name), "a")
    f.write(mobile+'\n')
    write_count = write_count + 1
    if write_count % 500 == 0:
        print('{time}:result write {line} lines.'.format(time=datetime.datetime.now(),
                                                         line=write_count))
