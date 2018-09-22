import datetime
import mysql.connector

cnx = mysql.connector.connect(host='localhost',user='root',passwd='1', database='employees')
cursor = cnx.cursor()



query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(2018, 6, 5)
hire_end = datetime.date(2019, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
    print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))

cursor.close()
cnx.close()

print("-----------------------------")

cnx = mysql.connector.connect(host='localhost',
                              user='root',
                              passwd='1',
                              database='order_settle'
                              )
cursor = cnx.cursor()
query =("SELECT DATE_FORMAT( order_time, '%Y-%m' ) as aa , count( 1 ) as cc "
        "FROM excel_order_detail "
        "GROUP BY DATE_FORMAT( order_time, '%Y-%m' ); "
        )
cursor.execute(query)
for (aa,cc ) in cursor:
    print(aa,cc)

# print(cursor)

query=("show tables;")
cursor.execute(query)
for table in cursor:
    print(table)
cursor.close()
cnx.close()
