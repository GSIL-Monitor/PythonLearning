
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='帐户表';

CREATE TABLE `t_article` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `title` varchar(128) NOT NULL COMMENT '标题',
  `sub_title` varchar(128) DEFAULT NULL COMMENT '标题',
  `type` int(11) NOT NULL COMMENT '类型',
  `category_id` bigint(20) NOT NULL COMMENT '栏目id',
  `author_id` bigint(20) NOT NULL COMMENT '作者',
  `ancestor_ids` varchar(128) NOT NULL COMMENT '所有祖先id列表,逗号分隔',
  `description` varchar(256) DEFAULT NULL COMMENT '描述',
  `tags` varchar(128) DEFAULT NULL COMMENT '标签',
  `content` text COMMENT '内容',
  `image_url` varchar(512) DEFAULT NULL COMMENT '封面图URL',
  `conf` text COMMENT '配置',
  `pt` bigint(20) NOT NULL COMMENT '发布时间',
  `stat` tinyint(4) DEFAULT '0' COMMENT '状态',
  `ct` bigint(20) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `ut` bigint(20) NOT NULL DEFAULT '0' COMMENT '更新时间',
  `ver` bigint(20) NOT NULL DEFAULT '0' COMMENT '版本号，用于乐观锁',
  `del` tinyint(4) NOT NULL DEFAULT '0' COMMENT '软删标识：0=未删；1=已删',
  PRIMARY KEY (`id`),
  KEY `category_id_INDEX` (`category_id`),
  KEY `title_INDEX` (`title`),
  KEY `author_id_INDEX` (`author_id`)
) ENGINE=InnoDB AUTO_INCREMENT=357 DEFAULT CHARSET=utf8mb4 COMMENT='文章';