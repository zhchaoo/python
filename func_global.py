#!/usr/bin/python
# Filename: func_local.py

def fun():
    global x

    print 'x is ', x
    x = 2
    print 'Changed local x to ', x

x = 50
fun()
print 'Value of x is ', x
