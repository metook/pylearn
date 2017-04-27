#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
#time:2017/4/20 22:58
# import credicard_operation,login
from credicard_operation import *
import pickle,login,sys
from datetime import datetime
def menu(username):
    print '''
    \t\033[0;34;0mHello,%s 欢迎来到信用卡操作界面\033[0m
------------------------------------------------
    \033[0;31;0m1、取现\t2、查询\t3、转账\t4、还款\t5、退出\033[0m
    '''%username
###写日志模块
def log_write(filename,username,logs):
    log_time = str(datetime.now()).split('.')[0] + '\t'
    data = read('log_info')
    log_str = log_time + logs
    data[username].append(log_str)
    print data
    f = open(filename, 'w')
    pickle.dump(data, f)
    f.close()
if __name__ == '__main__':
    try:    ######尝试曲login函数的返回值
        username = login.login()[0]
    except:  #####没有取到 username 退出
        sys.exit()
    while True:
        menu(username)
        choose = int(raw_input('\033[0;32;0m请选择要执行的操作（chose 1 2 3 ...）：\033[0m'))
        if choose == 1:
            number = int(raw_input('Enter get money number:'))
            ##取现操作，钱数减少
            #credicard_operation.get_money(username,number)
            ##操作写入日志文件 log_info
            if get_money(username,number):
                data = read('user_account')
                current_money = data[username]
                log_str = '取现￥%s成功！！！,剩余金额：￥%s.'%(number,current_money)
                log_write('log_info', username, log_str)
            else:
                data = read('user_account')
                current_money = data[username]
                log_str = '取现￥%s失败,余额不足!!!剩余金额：￥%s.'%(number,current_money)
                log_write('log_info', username, log_str)
        elif choose == 2:
            inquiry(username)
        elif choose == 3:
            to = raw_input('Enter who do you want to pay:')
            to_money = int(raw_input('Enter how much you want to pay:'))
            try:
                money_reduce(username,to_money)
                money_add(to,to_money)
                data = read('user_account')
                current_money_from = data[username]
                current_money_to = data[to]
                log_str_from = '转账给 %s,金额：￥%s,余额为：%s.'%(to,to_money,current_money_from)
                log_str_to = '收到 %s的转账,金额：￥%s,余额为：￥%s.'%(username,to_money,current_money_to)
                log_write('log_info',username,log_str_from)
                log_write('log_info',to,log_str_to)
            except:
                print 'Error.'
        elif choose == 4:
            try:
                data = read('user_account')
                pay_back_number = int(raw_input('Enter how much you want to pay back:'))
                money_add(username, pay_back_number)
                current_money = data[username]
                log_str = '还款￥%s成功，剩余金额：￥%s.'%(pay_back_number,current_money)
                log_write('log_info', username, log_str)
            except:
                print 'Error input!!!!'

        elif choose == 5:
            sys.exit('退出')
        else:
            print 'Error input.'
