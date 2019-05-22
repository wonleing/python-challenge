#!/usr/bin/python
import urllib
baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = "12345"
#num = "46059"
num = "90052"
while int(num):
    content = urllib.urlopen(baseurl+num).read()
    num = content.split(" ")[-1]
    print num
