#!/usr/bin/python
import urllib,pickle
obj = pickle.load(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
for line in obj:
    ret=""
    for item, num in line:
        ret += item * num
    print ret
