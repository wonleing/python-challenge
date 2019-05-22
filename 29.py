#!/usr/bin/python
import urllib2,bz2
url = "http://www.pythonchallenge.com/pc/ring/guido.html"
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, 'repeat', 'switch')
pwhandler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(pwhandler)
spaces = opener.open(url).read().split("</html>")[1].split("\n")
data = ""
for i in spaces:
    data += chr(len(i))
info = bz2.decompress(data[1:])
print info
