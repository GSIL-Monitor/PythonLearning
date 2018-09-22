import re

str1 = 'CREATE TABLE `avatar` ('.lower().replace('if not exists','')
a = re.findall('create\Wtable\W+(\w+)\W+', str1)[0]
table_name = re.findall('create\W*table\W*(\w+)\W*', str1)[0]

print(a)
print(table_name)


str2 = '  `id` bigint(20) NOT NULL AUTO_INCREMENT comment "注释内容0",'
b = re.findall('\W+(\w+)\W+', str2)[0]
print(b)


str3='  PRIMARY KEY (`id`),'.lower()
print(str3.find('key')>0)