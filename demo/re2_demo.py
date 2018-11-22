#!/usr/bin/python
import re

line = "Cats are smarter than dogs";

matchObj = re.findall(r'dogs', line)
if matchObj:
    print("match --> matchObj.group() : ", matchObj)
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)

if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")