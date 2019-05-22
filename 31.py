#!/usr/bin/python
print "Please google grandpa rock, and you will get it Thailand Koh Samui"
print "Google the mandelbrot set. say http://hi.baidu.com/liulihao/blog/item/79f9a4debbde1a54cdbf1a3d.html"
x_start, y_start, x_end, y_end = 0.34, 0.57, (0.34+0.036), (0.57+0.027)
import Image
im = Image.open("mandelbrot.gif").transpose(Image.FLIP_TOP_BOTTOM)
ori = list(im.getdata())
w, h = im.size
dx, dy = 0.036/w, 0.027/h

def test(x,y):
    if x*x + y*y < 4:
        return True
    else:
        return False

res = []
for j in range(h):
    for i in range(w):
        # N0 is x0+y0*i, N is x+y*i
        x = x0 = x_start + dx * i
        y = y0 = y_start + dy * j
        pt = 0
        while test(x,y):
            # next N is N*N+N0, that is (x*x-y*y+x0)+(2*x*y+y0)*i
            nx = x * x - y * y + x0
            ny = 2 * x * y + y0
            x, y = nx, ny
            pt += 1
            if pt == 128:
                break
        res.append(pt)
dif = []
for k in range(len(ori)):
    if ori[k] != res[k] and res[k] != 128:
        d = ori[k] - res[k]
        if d < 0:
            d += 256
        dif.append(d)
dl = len(dif)
print dl
open("test.dat","w").write(str(dif))
print "The length of diff is:",dl
for i in range(3,int(dl**0.5),2):
    if dl % i == 0:
        print dl,"can be divided by",i
        break
newim = Image.new("P",(i,dl/i))
newim.putdata(dif)
newim = newim.rotate(180).resize((10*i,10*dl/i))
newim.save("31.png")
print "Please check out 31.png and google out what it is. (arecibo code)"
