#!/usr/bin/env python
# -*- coding: UTF-8 -*-
count = 0
retry_limit = 3
lock_file = open('lockfile','w+')
userinfo = open('userinfo','r')
while count < retry_limit:
    username = raw_input("Enter your username:")
    for i in lock_file.readlines():
        if username in i.split()[0]:
            print "account is locked,process will be quit"
            exit()
    password = raw_input("Enter passwd:")
    match = False
    for line in userinfo.readlines():
        user,passwd = line.strip('\n').split()
        if username == user and password == passwd:
            print "yyyyyyyyyyyyyyyyyyes......."
            match = True
            break
    if match ==False:
        print "unmatched."
        count += 1
    else:
        print "login.............."
        break
        userinfo.close()
else:
    print "your account will be locked"
    lock_file.write(username)
    lock_file.write('\n')
    lock_file.close()




