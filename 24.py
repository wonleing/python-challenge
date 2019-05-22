#!/usr/bin/python
import Image,sys,os
sys.setrecursionlimit(50000)
im = Image.open("maze.png")
mx,my = im.size
do = 1
white = (255, 255, 255, 255)

def rm(im,x,y):
    rt = 0
    for pt in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
        #print "++",pt,"++"
        if im.getpixel(pt) != white:
            rt += 1
            nx,ny = pt
    #print (x,y),"---------------",rt
    if rt == 1:
        #print "now rm ", (x,y), " and its next is ", (nx,ny)
        im.putpixel((x,y), white)
        if rt ==1 and not (nx == 0 or ny == 0 or nx == mx-1 or ny == my-1):
            rm(im,nx,ny)
        return 1
    elif rt == 0:
        im.putpixel((x,y), white)
        return 1
    else:
        return 0

for a in range(mx-2):
    for b in range(my-2):
        if im.getpixel((a+1,b+1)) != white:
            rm(im, a+1, b+1)
im.save("24.png")
# See 24.png, then know it start from (639,0)
(x,y) = (639,0)
end = (1,640)
newmap = []
while (x,y) != end:
    pt = im.getpixel((x,y))[0]
    newmap.append(chr(pt))
    im.putpixel((x,y), white)
    for (nx,ny) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if nx > 0 and nx != mx and ny > 0 and ny != my and im.getpixel((nx,ny)) != white:
            x,y = nx,ny
# Get pixels from newmap every other one
open("24.zip","wb").write("".join(newmap[1::2]))
os.system("unzip 24.zip")
os.system("unzip mybroken.zip")
