#!/usr/bin/python

def log0(func):
    print(func.__name__)
    return func

def log(func):
    def wrap(*args):
        print(func.__name__)
        return func(*args)
    return wrap

def logstring(string):
    def expense(func):
        def wrap(*args):
            print("%s %s" %(string, func.__name__))
            return func(*args)
        return wrap
    return expense

@log0
def test0():
    print("test")


@log
def test(string = ''):
    print("test:%s" %string)

@logstring('with params')
def test1(string = ''):
    print("test:%s" %string)

if __name__ == "__main__":
    test0()
    test()
    test1()


