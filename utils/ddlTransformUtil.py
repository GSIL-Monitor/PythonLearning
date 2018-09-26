# -*- coding: utf-8 -*-

import re
import sys


def ddl_transform(sql):
    out_ddl = ''
    for i in sql.strip().split('\n'):
        i = i.strip().lower()
        if i.find('create table') >= 0:
            table_name = re.findall('create\W*table\W*(\w+)\W*', i)[0]
            out_ddl = out_ddl + 'CREATE TABLE IF NOT EXISTS {table}('.format(table=table_name) + '\n'
        elif i.find('key') < 0 and i.find('engine') < 0:
            col_name = re.findall('\W*(\w+)\W+', i)
            if len(col_name) > 0:
                col_name = col_name[0]
            else:
                col_name = None

            is_not_id_value = i.find('int') >= 0 and i.find('id') < 0
            if is_not_id_value:
                col_type = 'BIGINT'
            else:
                col_type = 'STRING'

            col_comm = re.findall('comment\W*\'(.+)\'', i)
            if len(col_comm) > 0:
                col_comm = col_comm[0]
            else:
                col_comm = None
            col = '    {col_name:<15} {col_type} COMMENT \'{col_comm}\',\n'.format(
                col_name=col_name,
                col_type=col_type,
                col_comm=col_comm)
            out_ddl = out_ddl + col
        elif i.find('engine') >= 0:
            table_comment = re.findall('comment\W\'(.+)\'\W*', i)

            if len(table_comment) > 0:
                table_comment = table_comment[0]
            else:
                table_comment = None
            end = ') COMMENT \'{table_comment}\'\n' \
                  'PARTITIONED BY (\n' \
                  '    ds STRING COMMENT "业务日期"\n' \
                  ');'.format(table_comment=table_comment)
            out_ddl = out_ddl + end
            pass
    out_ddl = out_ddl.replace(',\n)', '\n)')
    print(out_ddl)
    return out_ddl


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ddl_file = sys.argv[1]
        sql_list = open(ddl_file).read()
        sql_list = sql_list.strip().split(';')[:-1]
        ddlct = len(sql_list)
        if ddlct == 1:
            print('{file} has one ddl.'.format(file=ddl_file))
        else:
            print('{file} has {num} ddls.'.format(num=ddlct, file=ddl_file))

        for sql in sql_list:
            ddl_transform(sql.strip('\n'))
            print('\n')
    else:
        print('需输入ddl文件,且每个建表语句以;结束,支持有多个建表语句.')
        exit(1)
    pass
