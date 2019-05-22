#!/usr/bin/python
import Image
f=open("evil2.gfx","r")
data=f.read()
gf=[[],[],[],[],[]]
i=0
for node in data:
    gf[i].append(node)
    i += 1
    if i == 5:
        i=0
f.close()
i=0
for img in gf:
    dt=""
    for bi in img:
        dt += bi
    ff=open("12_%s" %i,"w")
    i += 1
    ff.write(dt)
    ff.close()

#dt=list(img.getdata())
#print type(dt),len(dt)
#newdt=[]
#for node in dt:
#    snode=str(node).replace("1,","0,")
#    newdt.append(eval(snode))
#print type(newdt),len(newdt)
#img2=Image.new("RGB", (x,y))
#img2.putdata(newdt,1.0,0)
##img2.save("12.png")
