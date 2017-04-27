#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author:lonerangerr
#time:2017/4/14 15:33

import logging
def foo():
    print ('This is function foo.')



def record_log(func):
    def wrapper(*args,**kwargs):
        logging.warn("%s is running"%func.__name__)
        func()
        return func(*args)
    return wrapper
@record_log
def bar():
    print 'aaa'
bar()
print map(lambda x:x**2,xrange(1,11))
