
import mysql.connector


#### mysql链接初始化,表查询
from mysql.connector.django.introspection import DatabaseIntrospection

host='localhost'
cnx = mysql.connector.connect(host=host,user='root',passwd='1')
cnx.database = 'order_settle'
print(cnx.database)


cursor = cnx.cursor()
sql = 'desc {table_name};'.format(table_name='excel_order_detail')
print(sql)
a = cursor.execute(sql)

print(a)

# a=DatabaseIntrospection.get_constraints(cursor, 'excel_order_detail')
    # .get_table_description(cursor, 'excel_order_detail')

# tables=cnx.cmd_query('show databases;').items()
# cnx.cmd_stmt_execute('show databases;')
# print(tables)
# print(cnx.cmd_stmt_execute('show databases;'))
exit(1)

database='wechat'

cnx.database=database