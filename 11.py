#!/usr/bin/python
import Image
img=Image.open("cave.jpg")
(x,y) = img.size
data=""
i=0
for i in range(x):
    j=0
    for j in range(y):
        if (i+j)%2:
            img.putpixel((i,j),(0,0,0))
img.save("11.png")
