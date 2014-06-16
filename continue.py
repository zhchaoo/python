#!/usr/bin/python

while True:
    s = raw_input("Enter you string: ")
    if s == "quit":
        break
    elif len(s) < 3:
        continue
    print 'Input is of sufficient length'

print 'Done'
