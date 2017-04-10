#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
#time:2017/4/9 20:41
count = 2000
product = [
    ["apple", 500],
    ["watch", 150],
    ["mac", 800],
    ["camera", 2000]
]
shop_list = []
while True:
    for index,p in enumerate(product):
        print index,p[0],p[1]
    choice = raw_input("Choose which you want to buy:").strip()
    if choice.isdigit():
        choice = int(choice)
        p_price = product[choice][1]
        if p_price <= count:
            shop_list.append(product[choice])
            count -= p_price
            print "Add %s into shop list,you still have %s"%(product[choice][0],count)
        else:
            print "you have no enough money..."
    elif choice == 'quit':
        print "--------------shop lsit----------------"
        for k,v in shop_list:
            print k,v
        print "you current count is $%s ..."%count
        print "-------------- the end -----------------"
        break