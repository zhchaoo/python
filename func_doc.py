#!/usr/bin/python
# Filename: func_doc.py

def maxmium(x, y):
    '''this function return the biggest number of two string \
Input must be integer'''
    if x > y:
        return x
    else:
        return y

print maxmium.__doc__
print maxmium(3, 5)
