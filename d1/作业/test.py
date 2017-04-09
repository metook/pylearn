##!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
count = 0
retry_limit = 3
while count < retry_limit:
    username = raw_input("Enter your username:")
    with open('lockfile','r') as f:
        for i in f.readlines():
            if username == i.split()[0]:
                print "Sorry,%s:your account is locked,process will be quit..."%username
                f.close()
                exit()
    password = raw_input("Enter your passwd:")
    match = False
    with open('userinfo','r') as f:
        for line in f.readlines():
            user,passwd = line.strip('\n').split()
            if username == user and password == passwd:
                #print "yyyyyyyyyyyyyyyyyyes..."
                pass
                match = True
                break
        if match ==False:
            print "Unmatched!!! u still have %s times to retry..."%(2-count)
            count += 1
        else:
            print "Hello,%s: Welcome to login..."%username
            break
    f.close()
else:
    print "Sorry,%s:your account will be locked..."%username
    with open('lockfile','a') as f:
        f.write(username)
        f.write('\n')
        f.close()




