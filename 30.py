#!/usr/bin/python
import Image
data = open("yankeedoodle.csv").read()
d2 = data.replace("\n"," ")
dl = d2[:-1].split(", ")
l = len(dl)
print "The array length is: %d" % l
for i in range(int(l**0.5)):
    i += 1
    if l % i == 0 and i != 1:
        print "I can divided by: ",i
        print "The picture width and hight size are: ", i, " and ", l/i
p = Image.new("P",(53,139)) # 139X53 turns out to be rubish
newl = []
for i in dl:
    newl.append(int(256*float(i)))
p.putdata(newl)
p = p.transpose(Image.FLIP_TOP_BOTTOM).rotate(-90)
p.save("30.png")
print "Take a look at the formula in 30.png"
j = 0
n = []
for i in dl:
    if j % 3 == 0:
        n1 = i[5]
    elif j % 3 == 1:
        n2 = i[5]
    else:
        n3 = i[6]
        n.append(chr(int(n1+n2+n3)))
    j += 1
print "".join(n)
