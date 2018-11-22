import datetime
import mysql.connector

cnx = mysql.connector.connect(host='localhost',
                              user='root',
                              passwd='1',
                              database='test'
                              )
cursor = cnx.cursor()
cursor.execute("select * from `dual`")

print(cursor.arraysize)
print(cursor.rowcount)
print(cursor.statement)
print(cursor.column_names)
print(cursor.arraysize)

print('-'*50)
for a in cursor:
    print(a[0])
