#!/usr/bin/python
import Image,bz2,keyword
im = Image.open("zigzag.gif")
index = im.global_palette.palette[::3]
imap = {}
for i in range(256):
    imap[i] = ord(index[i])

raw1 = list(im.getdata())
raw2 = []
for j in raw1:
    raw2.append((imap[j]))
raw1 = raw1[1:]
raw2 = raw2[:-1]
res = ["",[]]
for k in range(len(raw1)):
    if raw1[k] != raw2[k]:
        res[0] += chr(raw1[k])
        res[1].append(k)

im2 = Image.new("P", im.size)
colors = [255] * len(raw1)
for px in res[1]:
    colors[px] = 0
im2.putdata(colors)
im2.save("27.png")
print "Check out 27.png, it will tell you that NO KEY WORD"
bzdata = "".join(res[0])
rawdic = bz2.decompress(bzdata).split()
print list(set(rawdic) - set(keyword.kwlist))
