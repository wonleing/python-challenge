#!/usr/bin/python
import urllib,zipfile
url = "http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg"
info = urllib.urlopen(url).info()['Content-Range']
s, e = info.split("-")[1].split("/")
s = int(s) + 1
e = int(e)
#print s,e

opener = urllib.FancyURLopener({})
while True:
    opener.addheaders = [('range', 'bytes=%d-%d' %(s, e))]
    try:
        rs = opener.open(url)
    except:
        break

    try:
        s, e = rs.info()['Content-Range'].split("-")[1].split("/")
        s = int(s) + 1
        e = int(e)
        print rs.read()
    except:
        break

s = e
while True:
    opener.addheaders = [('range', 'bytes=%d-%d' %(s, e))]
    try:
        body = opener.open(url).read()
        print body
        s -= 50
    except:
        break
    if not body:
        break

s = 1152983631 # This is get from the last body
opener.addheaders = [('range', 'bytes=%d-%d' %(s, e))]
data = opener.open(url).read()
open("20.zip", "wb").write(data)

nickname = "invader" # Get from previous message. invader.html: "Yes! that's you!"
password = nickname[::-1]
f = zipfile.ZipFile('20.zip')
f.extractall(pwd=password)
print "Please check follwoing files: ",f.namelist()
