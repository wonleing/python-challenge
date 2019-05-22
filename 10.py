#!/usr/bin/python
def mod(a=None):
    tmp = "0"
    part = []
    for i in str(a):
        if tmp != i:
            part.append([i])
            tmp = i
        else:
            part[len(part)-1].append(i)
    return part

a=[1]
i=0
while (i<31):
    cov = mod(a[i])
    new = ""
    for j in range(len(cov)):
        new += str(len(cov[j]))
        new += cov[j][0]
    a.append(new)
    i += 1
print len(a[30])
