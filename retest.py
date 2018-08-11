###求指教这个正则该怎么写,多少的反斜杠

a='''\{智代}「那么，今天就来庆祝自立吧」'''
print(a)
import re
replace_reg3 = re.compile(r'\\\{(.+)\}') 
a = replace_reg3.sub(r'\1'+':',a)
print(a)