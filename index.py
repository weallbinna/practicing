a = int(input())
n = 0
for b in range(a):
    f = True
    c = input()
    for b in range(len(c)):
        if f==False:
            break
        d = c.index(c[b])
        for e in range(len(c)):
            if c[b] == c[e]:
                if (e-d)<=1:
                    d = e
                else:
                    f =False
                    break
    if f == False:
        continue
    n+=1
print(n)            