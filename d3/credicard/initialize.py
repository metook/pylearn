#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
#time:2017/4/25 10:49
import pickle
info ={
    'user1':10000,
    'user2':20000,
    'user3':30000
}
log = {
    'user1':['--- Log Info for user1 ---'],
    'user2':['--- Log Info for user2 ---'],
    'user3':['--- Log Info for user3 ---']
      }
def write(filename,fileinfo):
    f = open(filename,'w')
    pickle.dump(fileinfo,f)
    f.close()

if __name__ == '__main__':
    #write(info) ##初始化user_account文件
    write('log_info',log)
    write('user_account',info)