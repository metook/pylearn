#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
#time:2017/4/10 9:35
'''
d = {}
d['a'] = 'this is a.'
d1 = {'a':1,'b':2,'c':3}
for k,v in d1.items():
    print k,v       ###输出字典的所有键、值
print d1.keys()     ###输出字典的所有键
print d1.values()   ###输出字典的所有值
print d1.items()    ###d1.items() 类型为字典
print d1.has_key('d')
d1.clear()          ###清空字典
###多级字典的读取与修改
d2 = {
     'user1':{'age':24,'job':'doc'},
     'user2':{'age':30,'job':'teacher'}
 }
print d2
d2['user1']['age'] = 44
print d2
###列表字符串的转化
s1 = "hello a b c"
S = s1.split()
print '.'.join(S)
'''
#存储字典（pickle序列化）
import pickle
a = {'a':1,'b':2}
with open('tmp','wb') as f:
    pickle.dump(a,f)
f.close()
#pickle的反序列化，读取文件内容
with open('tmp','rb') as b:
    print pickle.load(b)
