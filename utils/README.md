# Python工具库

### 加载到自己的项目
在mac中多个Python项目，需要用utils时,
可以把utils建立软连接到自己项目的根目录下.
1. 这样修改任意一个项目里utils的代码都会在utils下生效
2. 可以像使用当前项目空间的其他包一样正常使用import功能

- 可以使用如下命令行建软连接 __(注意：这里的操作不同于Mac的『制作替身』)__ 

```cmd
cd */your_project_root
ln -s /Users/admin/PycharmProjects/utils ./utils
```
提交代码可以分别在utils项目和your_project项目分别提交


### conf

如果需要链接`MySQL`，`odps`，`es`,
**需要自己在uitl目录下新建文件conf.py**，
并填上自己的配置参数。

`conf.py`内容如下
```python
# [elasticsearch]
es_node = [{'host': '127.0.0.1', 'port': 9200}]

# [odps] 
access_id = '<access_id>'
secret_access_key ='<secret_access_key>'
project = 'babyfs_data'
end_point = 'http://service.odps.aliyun.com/api'

# [mysql]
local_db = {
    'ip': 'localhost',
    'post': '3306',
    'user': 'root',
    'password': '1',
    'database': 'robotlog'
}
```

