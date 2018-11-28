from mysql import connector
import sys

sys.path.append('/home/admin/babyfs_project/wxbot/src/')


def mysqlInit(db_conf):
    cnx = connector.connect(host=db_conf['ip'],
                            user=db_conf['user'],
                            passwd=db_conf['password'],
                            database=db_conf['database'])
    return cnx


if __name__ == '__main__':
    from utils.conf import *

    print(local_db)
    cnx1 = mysqlInit(local_db)
    print(cnx1.server_port)

