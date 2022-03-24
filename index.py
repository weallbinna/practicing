def Han(a):
    a = str(a)
    if len(a) ==1:
        return 1
    b = []
    for i in range(len(a)-1):
        b.append(int(a[i+1])-int(a[i]))
    b = set(b)
    if len(b) ==1:
        return 1
    else:
        return 0

n = 0
i = int(input())
for l in range(1,i+1):
    n += Han(l)
print(n)
        
        
        