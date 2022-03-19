a = list(input())
b = []
if len(a)<2:
    a.insert(0,"0")
n = 1
b.append(a[1]) 
c = list(str(int(a[0]) + int(a[1])))
if len(c)<2:
    c.insert(0,"0")
b.append(c[1])
while  int(a[0]) != int(b[0]) or int(a[1]) != int(b[1]) :
    c.clear
    c = list(str(int(b[0]) + int(b[1])))
    if len(c)<2:
        c.insert(0,"0")
    d = (b[1])
    b = list(d + c[1])
    n +=1
print(n)