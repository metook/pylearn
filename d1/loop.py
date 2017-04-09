#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
luck_num = 19
input_num = -1
count = 0
while count < 3:
    input_num = int(input("Enter a number:"))
    if input_num > luck_num:
        print "your anwser is big."
    elif input_num == luck_num:
        print "right."
        break
    else:
        print "your anwser is small."
    count +=1

if input_num == luck_num:
    pass
else:
    print "you have guess 3 times,try again later!"
'''


#下边的是用for循环改写并简单优化过程
luck_num = 19
input_num = -1
for count in range(3):
    input_num = int(input("Enter a number:"))
    if input_num > luck_num:
        print "your anwser is big."
    elif input_num < luck_num:
        print "your anwser is small."
    else:
        print "right."
        break
else:
    print "you have guess 3 times,try again later!"