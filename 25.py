#!/usr/bin/python
import os,Image,wave
data = []
for i in range(25):
    i += 1
#    os.system("wget http://www.pythonchallenge.com/pc/hex/lake%d.wav --user butter --password fly" %i)
    wv = wave.open("lake%d.wav" %i)
    raw = wv.readframes(wv.getnframes())
    i = 0
    newpx = []
    pxs = []
    for j in raw:
        newpx.append(ord(j))
        if i % 3 == 2:
            pxs.append(tuple(newpx))
            newpx = []
        i += 1
    data.append(pxs)
    wv.close()

unit = int(len(pxs)**0.5)
print "the newmap (5 X 5) unit size is: ", (unit, unit)
res = []
for y in range(5):
    for uy in range(unit):
        start = unit * uy
        end = start + unit
        for i in range(5):
            cfile_no = 5*y + i
            res += data[cfile_no][start:end]

im = Image.new("RGB", (unit*5, unit*5))
im.putdata(res)
im.save("25.jpg")
