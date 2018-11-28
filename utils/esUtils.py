import datetime
import time
from elasticsearch import helpers
import elasticsearch
from utils.odpsInit import odpsInit
from utils.conf import es_node


def esInit(node=es_node):
    es = elasticsearch.Elasticsearch(node)
    print('connected elasticsearch on {0} success'.format(node))
    print(es.info())
    return es


def update_index(index_id, time_format='%Y-%m-%d %H:%M:%S'):
    es = esInit()
    # 获取上次的查询的时间点
    from_time = es.get(index='loop_time_index', doc_type='base_type', id=index_id)['_source']['last_update_time']
    # 更新查询时间节点
    to_time = datetime.datetime.now().strftime(time_format)
    es.index(index='loop_time_index', doc_type='base_type', id=index_id,
             body={'last_update_time': to_time})
    return from_time


def load2es(sql='', es_root_index='robot_user_info', es_index_id='user_name', bulk_len=400):
    """
    odpssql查询结果批量插入到es
    :param sql: ODPS查询sql
    :param es_root_index: es的index, type 默认使用 base_type
    :param es_index_id: index的文档id使用指定字段处理
    :return:
    """

    # 工具方法,仅在导入数据时使用
    def get_row_json(row):
        """
        :param row: ODPS查询的一行结果记录
        :return: 返回字典结果数据
        """
        a = {}
        for field in row:
            a[field[0]] = str(field[1])
        a['timestamp'] = datetime.datetime.now()
        return a
        pass

    # odps 准备s
    o = odpsInit()

    # es 准备
    es = esInit()

    # 查询odps,插入es
    print(datetime.datetime.now(), sql)
    with o.execute_sql(sql).open_reader() as reader:
        ttt = tt = time.time()
        print('{t}\tselect {count} rows.'.format(t=ttt, count=reader.count))
        j = i = 0
        actions = []
        for r in reader:
            # print(r.values)
            r_json = get_row_json(r)
            # print(json.dumps(r_json, ensure_ascii=False))
            # for
            action = {
                "_index": es_root_index,
                "_type": "base_type",
                "_id": r_json[es_index_id],
                "_source": r_json
            }
            i = i + 1
            actions.append(action)
            # 200 cost 179  3.0min
            # 400 cost 171  3.0min
            # 500 cost 205  3.5min
            if (len(actions) == bulk_len):
                j = j + 1
                helpers.bulk(es, actions)
                print(
                    '{t}\t第\t{j:<7}\t次写入.cost time: {ttt}'.format(
                        t=datetime.datetime.now(),
                        j=j,
                        ttt=(ttt - time.time()) / len(actions))
                )
                ttt = time.time()
                del actions[0:len(actions)]

        print('{t}\tcost time: {ttt} write {count} document into es index:{es_root_index}.'.format(
            ttt=(tt - time.time()),
            t=datetime.datetime.now(),
            count=reader.count,
            es_root_index=es_root_index))
    return True
    pass


if __name__ == '__main__':
    es = esInit()
    pass
