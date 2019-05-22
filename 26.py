#!/usr/bin/python
print "send mail to leopold.moz@pythonchallenge.com with subject and body as sorry:"
print """Never mind that.
Have you found my broken zip?
md5: bbb8b499a0eef99b52c7f13f4e78c24b
Can you believe what one mistake can lead to?"""
good = "bbb8b499a0eef99b52c7f13f4e78c24b"
import md5,zipfile,sys
f = open("mybroken.zip")
odata = f.read()
dic = []
for n in range(256):
    dic.append(chr(n))
i = 0
try:
    for chr in odata:
        for rp in dic:
            ndata = list(odata)
            ndata[i] = rp
            cmd5 = md5.new("".join(ndata)).hexdigest()
            if cmd5 == good:
                raise Exception
        i += 1
        sys.stdout.write(".")
except Exception:
    f.close()

open("26.zip","wb").write("".join(ndata))
zipfile.ZipFile("26.zip").extractall()
print "Please check ",zipfile.ZipFile("26.zip").namelist()[0]
