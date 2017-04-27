#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
#time:2017/4/9 20:41
count = 3000
shop_list =[]
goods = [
    ['pad',1000],
    ['phone',500],
    ['book',100],
    ['cup',50],
    ['camera',2000]
]
while True:
    for index,i in enumerate(goods):
        print index,i
    choice = raw_input('Select which you want to buy:').strip()
    if choice.isdigit():
        choice = int(choice)
        selected_price = goods[choice][1]
        if count >= selected_price:
            shop_list.append(goods[choice])
            count -= selected_price
            print 'Add %s to your shop list...You still have $%s...'%(goods[choice],count-selected_price)
        else:
            print 'You have no enough money...Try something others...'
    elif choice == 'quit':
        print 'your shop list:'
        for k,v in shop_list:
            print k,v
        print 'Bye.............'
        break
