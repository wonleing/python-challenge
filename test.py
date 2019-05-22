import Image
ufos=Image.open("mandelbrot.gif")
def mandelbrot(left=0.34, bottom=0.57, width=0.036, height=0.027, max=128, size=(640, 480)):
    xstep = width / size[0]
    ystep = height / size[1]
    for y in xrange(size[1] - 1, -1, -1):
        for x in xrange(size[0]):
            c = complex(left + x * xstep, bottom + y * ystep)
            z = 0+0j
            for i in xrange(max):
                z = z * z + c
                if abs(z) > 2:
                    break
            yield i

mandel = ufos.copy() # We can reuse the type, size and palette
mandel.putdata(list(mandelbrot()))
differences = [(a - b) for a, b in zip(ufos.getdata(), mandel.getdata()) if a != b]
len(differences)
print set(differences)
plot = Image.new('L', (23, 73))
plot.putdata([(i < 16) and 255 or 0 for i in differences])
plot.resize((230, 730)).save("test.png")
