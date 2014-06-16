#!/usr/bin/env python 
# Filename: finally.py

import time
import sys
if 'library/' not in sys.path:
    sys.path.append('library/')
from utility import isset

try:
    f=file('poem.txt')
    while True: # our usual file-reading idiom 
        line=f.readline()
        if len(line)==0: 
            break
        time.sleep(2)
        print line, 
except IOError, x:
    print 'Error %s' %x.message
finally:
    if isset('f'):
        f.close()
    print 'Cleaning up...closed the file'
