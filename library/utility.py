#!/usr/bin/python
# Filename: utility.py

def isset(v):
    '''return a variable is set or not'''
    return v in locals() or v in globals()

def issete(v):
    '''return a variable is set or not'''
    try:
        type(eval(v))
    except:
        return False
    else:
        return True

