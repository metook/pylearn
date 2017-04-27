#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
#time:2017/4/10 16:32
# 函数练习

#######################################################################
#!//usr/bin/env python
#coding:utf-8
# def foo001(**kwargs):
#     print"let's start!!!",kwargs
# foo001(haha=1,hehe=2,gg=3)
#
# def foo002(*args):
#     print 'This is a test for args!!!!',args
# foo002(1,2,3,4,5,'a','b','c')

#######################################################################
#**kwargs 传入的参数可以是字典
#*args  传入的参数可以是多个字符串或者数字
#######################################################################
# a = lambda x,y:x+y
# print a(1,2)
#
# li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
# #li=sorted(li,key=lambda x:x["age"])
# #print(li)
# li = sorted(li,key=lambda x:x['age'])
# print li
# print lambda x:x['age']
###降序排列
# l1 = [('a',4),('b',8),('c',1),('d',3)]
# sorted_l1 = sorted(l1,key=lambda x:x[1],reverse=True)
# #print sorted_l1
# import time
# def run():
#     print "11111"
#     yield 1
#     time.sleep(1)
#     print "22222"
#     yield 2
#     print "33333"
#     time.sleep(1)
#     print "44444"
#     time.sleep(1)
# task = run()
# task.next()
# task.next()
#
# print "do something else."
# import pickle,json
# d = {'name':'loneranger','age':24,'job':'IT'}
# with open('readme.md','a') as f:
#     json.dump(d,f)
#     f.close()
# import pickle
# info ={
#     'user1':10000,
#     'user2':20000,
#     'user3':30000
# }
# def write(info):
#     f = open('user_account','w')
#     pickle.dump(info,f)
#     f.close()
# def read():
#     f = open('user_account','r')
#     data = pickle.load(f)
#     f.close()
#     return data
# data = read()
# print data(
from datetime import datetime
import time
t = str(datetime.now())
# print t.split('.')[0]
str2 = 'aaaa'
print str(datetime.now()).split('.')[0] + '\t'+ str2
