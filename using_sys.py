#!/usr/bin/python
# Filename : using_sys.py

import sys

#print 'The command num is ', sys.num
print 'The command args are: '
for i in sys.argv:
    print i

print '\nThe PYTHON PATH is ', sys.path, '\n'
