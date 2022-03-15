import sys
a,b = map(int,sys.stdin.readline().split(" "))
c = []
f = 0
for d in range(a):
    c.append(sys.stdin.readline().strip(" "))
    if int(c[d])<b:
     print(c[d], end =" ")    

