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

            if i.find('int') >= 0:
                col_type = 'BIGINT'
            else:
                col_type = 'STRING'

            col_comm = re.findall('comment\W*\'(.+)\'', i)
            if len(col_comm) > 0:
                col_comm = col_comm[0]
            else:
                col_comm = None
            col = '    {col_name} {col_type} COMMENT \'{col_comm}\',\n'.format(
                col_name=col_name,
                col_type=col_type,
                col_comm=col_comm)
            out_ddl = out_ddl + col
        elif i.find('engine') >= 0:
            table_comment = re.findall('comment=\'(.+)\'\W*', i)

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
    sql = '''
    CREATE TABLE `t_account` (
      `id` bigint(20) NOT NULL,
      `user_id` bigint(20) NOT NULL COMMENT '用户id',
      `name` varchar(128) NOT NULL COMMENT '帐户名',
      `type` int(11) NOT NULL DEFAULT '0' COMMENT '帐户类型',
      `salt` varchar(50) DEFAULT NULL COMMENT 'slat',
      `password` varchar(50) DEFAULT NULL COMMENT '密码',
      `stat` tinyint(4) DEFAULT '0' COMMENT '状态',
      `ct` bigint(20) NOT NULL DEFAULT '0' COMMENT '创建时间',
      `ut` bigint(20) NOT NULL DEFAULT '0' COMMENT '更新时间',
      `ver` bigint(20) NOT NULL DEFAULT '0' COMMENT '版本号',
      `del` tinyint(4) NOT NULL DEFAULT '0' COMMENT '删除标志',
      PRIMARY KEY (`id`),
      UNIQUE KEY `name_UNIQUE` (`name`),
      UNIQUE KEY `user_id_type_UNIQUE` (`user_id`,`type`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='帐户表'
    '''
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
