def odpsInit(project='babyfs_data'):
    from odps import ODPS

    o = ODPS('LTAIGcHUtiuARZin',
             'pxx57vjysvBurt76Jhd93X9goMMGdc',
             project,
             endpoint='http://service.odps.aliyun.com/api')
    return o

def out_writer_init(tableName, ds, odps, project):
    output_table = odps.get_table(tableName, project)
    if output_table.exist_partition('ds=' + ds):
        output_table.delete_partition('ds=' + ds)
    writer = output_table.open_writer(partition='ds=' + ds, blocks=[0], create_partition=True)
    print('output into', tableName, 'partition ds=', ds, ':\n', output_table.schema)
    return output_table, writer

def mysqlInit():

    import mysql.connector
    cnx = mysql.connector.connect(host='localhost',
                                  user='root',
                                  passwd='1',
                                  database='order_settle'
                                  )
    # cnx.database ='order_settle'

    return cnx
