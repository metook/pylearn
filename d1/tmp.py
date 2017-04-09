#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
name = 'Bob'
age = 21
home = 'hebei'
print "my name is %s,\nage is %s,\nhome is in %s."%(name,age,home)
msg = "     aaa bb cc     "
print msg.strip()


list = ['a','b','c','b','q']
#在列表的最后边添加一个元素
list.append('d')
#查看有多少个b
print list.count('b')
#查看a的索引值
print list.index('a')
#索引为2的后边插入一个元素
list.insert(2,'hehe')
#删除一个元素,有多个元素b的时候只能删除第一个b
list.remove('b')
#反转列表元素
list.reverse()
#按照asic码方式排序
list.sort()
#删除列表中的三个b
for i in range(list.count('b')):
    list.remove('b')
#取出了索引为0、1、2的元素，不包括索引为3的元素！
print list[0:3]
print list[:3]
#在索引0到3的元素中每隔两个去一个元素
'''
list = [1,2,3,45,1,2,34,1]
list.pop()
print list

