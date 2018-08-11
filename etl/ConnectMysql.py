

import mysql.connector

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

cursor.execute(query)
for row in cursor:
    print(row)

cnx.close
