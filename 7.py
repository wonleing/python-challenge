#!/usr/bin/python
from PIL import Image
strade = 21 # this depends on the image hight that you cut
data = Image.open("oxygen.png").tostring()
i = 0
ret = ""
while i < len(data):
    ret += data[i]
    i += strade
print ret

ret = [105, 110, 116, 101, 103, 114, 105, 116, 121] # this is the result of uper code
STR = ""
for num in ret:
    STR += chr(num)
print STR
