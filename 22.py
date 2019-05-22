#!/usr/bin/python
from PIL import Image, ImageSequence
im = Image.open("white.gif")
dt = []
for frame in ImageSequence.Iterator(im):
    li = list(frame.getdata())
    x, y = li.index(8)%200, li.index(8)/200
    dt.append((x-100, y-100))

img = Image.new("P", (300, 50))
x,y = (0,0)
for i in range(len(dt)):
    #print dt[i]
    if dt[i] == (0, 0):
        x += 40
        y = 20
    else:
        x += dt[i][0]
        y += dt[i][1]
    #print x,y
    img.putpixel((x,y), 255)
img.save("22.gif")
