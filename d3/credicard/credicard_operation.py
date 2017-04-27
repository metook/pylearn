#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
#time:2017/4/14 17:02
'''
取现：不能超限额，手续费 %5
查询：余额、交易明细
转账：可以转到不同账户
还款：现金还款
退出：
'''
import pickle,datetime,sys
info ={
    'user1':10000,
    'user2':20000,
    'user3':30000
}
# data ={
#     'user1':11111111111,
#     'user2':20000,
#     'user3':30000
# }
##修改文件
# def write(new_dict):
#     f = open('user_account','w')
#     pickle.dump(new_dict,f)
#     f.close()
def write(filename,fileinfo):
    f = open(filename,'w')
    pickle.dump(fileinfo,f)
    f.close()
##读取文件
def read(filename):
    f = open(filename,'r')
    data = pickle.load(f)
    f.close()
    return data
##余额增加
def money_add(username,add_number):
    data = read('user_account')
    data[username] = data[username]+add_number
    write('user_account',data)
##余额减少
def money_reduce(username,reduce_number):
    data = read('user_account')
    if data[username] >= reduce_number:
        data[username] = data[username] - reduce_number
        write('user_account',data)
    else:
        return False   ####减少的钱大于余额
###取现
def get_money(username, reduce_number):
    data = read('user_account')
    if data[username] >= reduce_number:
        data[username] = data[username] - reduce_number*1.05
        write('user_account',data)
        return True
    else:
        return False   ###取现金额大于余额
###转账给别人
def pay_other(source,to,number):
    if money_reduce(source,number):
        money_add(source,number)
    else:
        return False
###查询交易明细
def inquiry(username):
    data = read('log_info')
    for i in data[username]:
        print i

###退出
def quit():
    sys.exit()



#write(info)
#money_add('user2',111111111)
#money_reduce('user1',1000)
if __name__ == '__main__':
    pass






