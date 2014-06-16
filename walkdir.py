#!/usr/bin/python
import os
import os.path
import shutil
import logging
import optparse
import subprocess

def walkDir(dir, function, exclude):
    excludelist = []
    if exclude:
        excludelist = exclude.split(',')
    files = os.listdir(dir)
    files.sort()
    if not dir.endswith(os.sep):
        dir = dir + os.sep
    for item in files:
        fullpath = dir + item
        if os.path.isdir(fullpath):
            if item not in excludelist:
                walkDir(fullpath, function, exclude)
        else:
            filename = dir + item
            if function:
                function(filename)

def logname(filename):
	print filename

if __name__ == "__main__":
    option_parser = optparse.OptionParser(usage="Usage: %prog [options] resource-path")
    option_parser.add_option("-e", "--exclude", type='string', default=None, help="parse multple args") 
    options, args = option_parser.parse_args();

    if len(args) > 1:
        logging.fatal("Usage: push_resource.py [options] resouce-path")
    else:
        if len(args) < 1:
            path = "";
        else:
            path = args[0]
        walkDir(path, logname, options.exclude);
