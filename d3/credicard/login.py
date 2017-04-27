#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
#time:2017/4/23 16:23
##判断有无该用户
def judge_user_exist(username):
    f = open('user_info','r')
    for i in f.readlines():
        if username == i.split()[0]:
            return True  ##存在
        else:
            pass  ##不存在
    f.close()
###判断是否标记为锁定状态,True为锁定，False为没锁定
def judge_user_locked(username):
    f = open('user_info','r')
    for i in f.readlines():
        if username == i.split()[0]:
            if int(i.split()[2]) == 0:#######  等于0代表账户未锁定状态
                return True
            else:
                return False
    f.close()
###判断账户名密码是否匹配
def judge_matched(username,passwd):
    f = open('user_info', 'r')
    for i in f.readlines():
        if username == i.split()[0]:
            if passwd == i.split()[1]:
                return True
            else:
                return False
###锁定账户
def lock_user(username):
    f = open('user_info','r')
    lines = f.readlines()
    content = ""
    for line in lines:
        if username == line.split()[0]:
            line = line.split()
            line[2] = 1          ####改成1代表锁定
            for i in range(0,line.__len__()):
                line[i] = str(line[i])
            new_line = '\t'.join(line)
            new_line = new_line + '\n'
            content += new_line
        else:
            content += line
    f.close()
    f = open('user_info','w')
    f.write(content)    ###修改后的内容写入文件
    f.close()

def login():
    count = 0
    retry_limits = 3
    while count < retry_limits:
        username = raw_input('Enter username:')
        passwd = raw_input('Enter password:')
        if judge_user_exist(username):
            if judge_user_locked(username):
                if judge_matched(username,passwd):
                    #print 'login...'
                    return username,passwd
                else:
                    print 'Wrong passwd...'
                    count += 1
                    continue
            else:
                print 'user is locked'
                return True
        else:
            print 'no such user...'
            return False

    else:
        print 'You have try 3 times,user will be locked!!'
        lock_user(username)
        return False
if __name__ == '__main__':
    login()