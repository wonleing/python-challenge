#!/usr/bin/python
import zipfile,re
zfile = zipfile.ZipFile("channel.zip", "r")
#zfile.printdir()
for info in zfile.infolist():
    fname = info.filename
    if fname == "readme.txt":
        data = zfile.read(fname)
        print data

fn="90052"
regex="[0-9]+"
ret = ""
reobj = re.compile(regex)
while fn:
    data = zfile.read(fn+".txt")
    fn = data.split(" ")[-1]
    if not re.match(regex, fn):
        print "******"+data+"******"
        break
    else:
        ret += zfile.getinfo(fn+".txt").comment
print ret
