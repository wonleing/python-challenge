#!/usr/bin/python
import Image
img = Image.open("mozart.gif")
x,y = img.size
data = list(img.getdata())
newdata = []
for i in range(y):
    line = data[:x]
    data = data[x:]
    p = line.index(195) #Pink (195) is the start of every line. Find its index and reconnect each line
    newdata += line[p:] + line [:p]
newimg=Image.new("P",(x,y))
newimg.putdata(newdata)
newimg.save("16.gif")
