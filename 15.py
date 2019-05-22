#!/usr/bin/python
import datetime
ret = []
for k in range(10):
    year = int("1"+str(k)+"6")
    week = datetime.date(year,01,26).weekday()
    if week == 0 and (k*10+6)%4 == 0:
        ret.append(year)
for i in range(10):
    for j in range(10):
        year = int("1"+str(i)+str(j)+"6")
        week = datetime.date(year,01,26).weekday()
        if week == 0 and (j*10+6)%4 == 0:
            ret.append(year)

print "Please google: ",ret[-2],"01","27"

