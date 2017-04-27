#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
#time:2017/4/23 20:55
# def a(username):
#     f = open('user_info', 'r')
#     for i in f.readlines():
#         if username == i.split()[0]:
#             print type(i.split()[2])
#     f.close()
# a('user2')


# def judge_user_exist(username):
#     f = open('user_info','r')
#     for i in f.readlines():
#         if username == i.split()[0]:
#             print 'yes',username
#             return True  ##存在
#         else:
#             pass
#     f.close()
# judge_user_exist('user21')
# def judge_matched(username,passwd):
#     f = open('user_info','r')
#     for i in f.readlines():
#         if username == i.split()[0]:
#             if passwd == i.split()[1]:
#                 return True
#             else:
#                 return False
# print judge_matched('user2','111')
##修改文件的内容
# def lock_user(username):
#     f = open('user_info','r')
#     lines = f.readlines()
#     content = ""
#     for line in lines:
#         if username == line.split()[0]:
#             line = line.split()
#             line[2] = 0
#             for i in range(0,line.__len__()):
#                 line[i] = str(line[i])
#             new_line = '\t'.join(line)
#             new_line = new_line + '\n'
#             content += new_line
#         else:
#             content += line
#     f.close()
#     f = open('user_info','w')
#     f.write(content)
#     f.close()
# lock_user('user3')
# import pickle,credicard_operation
# from datetime import datetime
# def log_write(filename,username,logs):
#     log_time = str(datetime.now()).split('.')[0] + '\t'
#     data = credicard_operation.read('log_info')
#     print data[username][1]
# #     log_str = log_time + logs
# #     data['user3'].append(log_str)
# #     print data
# #     f = open(filename, 'w')
# #     pickle.dump(data, f)
# #     f.close()
# #
# log_write('log_info','user2','ccccc')
# import credicard_operation
# # def get_money(username, reduce_number):
# #     data = read('user_account')
# #     #print data
# #     if data[username] >= reduce_number:
# #         data[username] = data[username] - reduce_number*1.05
# #         credicard_operation.write('user_account',data)
# #         return True
# #     else:
# #         return False   ###取现金额大于余额
# if credicard_operation.get_money('user1',100):
#     print 'aaaaaa'
# else:
#     print 'bbbbbbb'
# # credicard_operation.read('user_account')
a = int(raw_input('number:'))
print a