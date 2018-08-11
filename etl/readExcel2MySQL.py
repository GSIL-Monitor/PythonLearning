#!/usr/bin/env python
#coding=utf-8
import xlrd
import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(host='localhost',
                              user='root',
                              passwd='1',
                              database='order_settle'
                              )
cursor = cnx.cursor()
print(cursor)

query =("SELECT DATE_FORMAT( order_time, '%Y-%m' ) as aa , count( 1 ) as cc "
        "FROM excel_order_detail "
        "GROUP BY DATE_FORMAT( order_time, '%Y-%m' ); "
        )


cursor.execute(query )

for (aa,cc ) in cursor:
    print(aa,cc)
# print(cursor)

query=("show tables;")
cursor.fetchone(query)

cnx.close

#读取EXCEL中内容到数据库中
# wb = xlrd.open_workbook('/×.xlsx')
# sh = wb.sheet_by_index(0)
# dfun=[]
# nrows = sh.nrows  #行数
# ncols = sh.ncols  #列数
# fo=[]
#
# fo.append(sh.row_values(0))
# for i in range(1,nrows):
#       dfun.append(sh.row_values(i))
#
# cursor=conn.cursor()
# #创建table
# cursor.execute("create table test4("+fo[0][0]+" varchar(100));")
# #创建table属性
# for i in range(1,ncols):
#     cursor.execute("alter table test4 add "+fo[0][i]+" varchar(100);")
# val=''
# for i in range(0,ncols):
#     val = val+'%s,'
# print(dfun)
#
# cursor.executemany("insert into resources_networkdevice values("+val[:-1]+");" ,dfun)
#
# conn.commit()