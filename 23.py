#!/usr/bin/python
import os,sys
for file in os.listdir("/usr/lib/python2.6"):
    if file.endswith(".py"):
        f = open("/usr/lib/python2.6/"+file)
        data = f.read()
        if not data.find("gur snpr bs") == -1:
            print "gur snpr bs is found in: ", file
            print data
        f.close()

s='va gur snpr bs jung?'
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print "va gur snpr bs jung? Translation is:"
print "".join([d.get(c, c) for c in s]),"\n"

import this
