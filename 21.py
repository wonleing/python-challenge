#!/usr/bin/python
import zlib,bz2
st=open('package.pack').read()
log = ""
length=[]
while True:
    try:
        st = zlib.decompress(st)
        log += " "
    except:
        try:
            st = bz2.decompress(st)
            log += "*"
        except:
            if len(st) in length:
                break
            st = st[::-1]
            log += "\n"
            length.append(len(st))

print st
print log
