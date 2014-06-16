#!/usr/bin/python

import optparse

def exclude_callback(option, opt, value, parser):
    print "-e args is %s" %(value.split(','))

def main(path, options):
  """this python script is a demo for parse args"""
  if options.more:
      print main.__doc__

  if options.file:
      print "-f args is %s" %options.file

  if path:
      print "path is %s" %path

if __name__ == "__main__":
  option_parser = optparse.OptionParser(usage="Usage: %prog [options] resource-path")
  option_parser.add_option("-f", "--file", default=None, help="Help about this python script")
  option_parser.add_option("-m", "--more", default=False, action="store_true", help="Force push fonts to the device")
  option_parser.add_option("-e", "--exclude", type='string', default=None, action="callback", callback=exclude_callback, help="parse multple args")
  options, args = option_parser.parse_args();

  if len(args) > 1:
    logging.fatal("Usage: push_resource.py [options] resouce-path")
  else:
    if len(args) < 1:
      path = "";
    else:
      path = args[0]
    main(path, options);
