from datetime import datetime

from elasticsearch import Elasticsearch
es = Elasticsearch()

es.cluster.health(wait_for_status='yellow', request_timeout=1)

es.indices.create(index='my-index', ignore=400)


es.index(index="my-index", doc_type="test-type", id=1, body={"any": "data01", "timestamp":datetime.now()})
#查询数据，两种get and search
#get获取
res = es.get(index="my-index", doc_type="test-type", id=1)

print(res)

# es.get(index='indexName', doc_type='typeName', id='idValue')

#
#
# es.search(index='test-index', filter_path=['hits.hits._id', 'hits.hits._type'])
#
#
# es.search(index='test-index', filter_path=['hits.hits._*'])
#
#
#
#
# es.indices.delete(index='my-index', ignore=[400, 404])
