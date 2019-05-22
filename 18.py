#!/usr/bin/python
import gzip, difflib

def hextochar(hexs):
    ret = ""
    for b in hexs.split():
        ret += chr(int(b,16))
    return ret

f = gzip.open("deltas.gz")
raw = f.readlines()
data = [[],[]]
for line in raw:
    data[0].append(line[:53])
    data[1].append(line[56:-1])

dout = list(difflib.ndiff(data[0],data[1]))
res = ["","",""]
for line in dout:
    if line.startswith("+ "):
        res[0] += hextochar(line[2:])
    elif line.startswith("- "):
        res[1] += hextochar(line[2:])
    elif line.startswith("  "):
        res[2] += hextochar(line[2:])

for i in range(3):
    f = open("18_%d.png" %i,"w")
    f.write(res[i])
    f.close()
