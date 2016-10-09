#!/usr/bin/env python
# -*- coding: utf-8 -*-
#字符串构造
d = {"name":"Peter","age":20}
t = "insert into tb(%s) VALUES (%s)"

key_list = []
value_list = []
for k,v in d.items():
    key_list.append(k)
    value_list.append("%%(%s)s" %(k))

print(key_list,",".join(key_list))
print(value_list,','.join(value_list))
sql = t % (','.join(key_list),','.join(value_list))
print(sql)
