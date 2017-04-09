#!/usr/bin/env python
# -*- coding: UTF-8 -*-
for i in range(3):
    ###输入用户名、密码
    username = raw_input("Enter your username:")
    password = raw_input("Enter your password:")
    ##检查账号是否被锁定
    with open('lockfile','r') as f:
        for line in f.readlines():
            if username in line.split()[0]:
                print "Your account is locked,please call administrator."
            else:
                pass
    f.close()
    ##验证用户名、密码
    with open('userinfo','r') as f:
        for line in f.readlines():
            if username == line.split()[0] and password == line.split()[1]:
                print "Login success!!"
                break
            else:
                print "You username or passwd is wrong!! try again."
                continue
else:
    print "you have tried 3 times,and your account is locked."
    with open('lockfile','a') as f:
        f.write(username)
        f.close()
