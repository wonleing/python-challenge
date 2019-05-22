#!/usr/bin/python
import Image
data=list(Image.open("wire.png").getdata())
img=Image.new('RGB',(101,101))
x=0
y=0
direction=0
num=100
while num:
    cur = data[:num]
    data = data[num:]
    for node in cur:
        img.putpixel((x,y),node)
        if direction%4 == 0: #draw to right
            x += 1
        elif direction%4 == 1: #draw to down
            y += 1
        elif direction%4 == 2: #draw to left
            x -= 1
        else: #draw to up
            y -= 1
    if direction%2 == 0:
        num -= 1
    direction += 1
    #print x,y,direction,num

img.save("14.png")
