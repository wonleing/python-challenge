#!/usr/bin/python
import Image
im = Image.open("bell.png")
im.getpixel((0,0)) # This is a bug, must getpixel before split
r,g,b = im.split()
raw = list(g.getdata())
news = ""
i = 0
for px in raw:
    i += 1
    if i % 2 == 1:
        ppx = px
        continue
    dif = px - ppx
    if dif == 42 or dif == -42:
        continue
    else:
        if dif < 0:
            dif = -dif
        news += chr(dif)
print news
print "The write of python is: Guido van Rossum"
print "Guido van Rossum".split()[0]
