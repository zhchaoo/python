#!/usr/bin/python

import subprocess

cmd="bash"
begin=141
end=143
while begin<end:

    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE)
    p.stdin.write("ping -c 3 192.168.43."+str(begin)+"\n")
    begin += 1

    p.stdin.close()
    p.wait()

    print "execution result: %s" %p.stdout.read()

