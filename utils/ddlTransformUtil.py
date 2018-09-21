import sys, re

sql='''
CREATE TABLE `avatar` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `robot_wechat_id` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `user_name` varchar(180) COLLATE utf8mb4_bin DEFAULT NULL,
  `imgflag` bigint(20) DEFAULT NULL,
  `last_updatetime` bigint(20) DEFAULT NULL,
  `reserved1` text COLLATE utf8mb4_bin,
  `reserved2` text COLLATE utf8mb4_bin,
  `reserved3` int(11) DEFAULT NULL,
  `reserved4` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UQE_avatar_user_name` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=10633 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
'''

import odps
import mysql

def scheam(sql):

    pass

def get_name(sql):
    sql=sql.replace('`','').strip().lower()
    # print(sql)

    # 匹配create语句中的表名和表名的简写
    creatematch = r"(?!')*create\b*table\b*(?P<table_name>\w+)\b*\((?!')*"
    table_name = re.compile(creatematch)
    TabName = None
    m = table_name.groups(sql)
    print(m)
    print(TabName)
    pass

table_name  =  get_name(sql)