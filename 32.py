#!/usr/bin/python
def draw(d):
    iD = d.index("# Dimensions\n")
    iH = d.index("# Horizontal\n")
    iV = d.index("# Vertical\n")
    H, V = [], []
    for i in range(iH+1,iV,1):
        content = d[i][:-1]
        if content:
            H.append(content)
    for i in range(iV+1,len(d),1):
        content = d[i][:-1]
        if content:
            V.append(content)
    
    num = d[iD+1].split()
    x, y = int(num[0]), int(num[1])
    assert (len(H),len(V)) == (x,y)
    table = [[" " for col in range(x)] for row in range(y)]
    
    for i in range(x):
        if H[i] == str(x):
            for col in range(x):
                table[col][i] = "*"
    
    for i in range(y):
        if V[i] == str(y):
            for row in range(y):
                table[i][row] = "*"
    
    
    for line in table:
        print " ".join(line)

# Process warmup.txt
draw(open("warmup.txt","r").readlines())
print "This is an UP arrow, so we continue to pursue up.txt"
# Process up.txt
#draw(open("up.txt","r").readlines())
