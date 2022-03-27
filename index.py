a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
b = input()
c = 0
for n in a:
    if n in b:
        d = b.count(n)
        b = b.replace(n,' ')
        c +=d
b = b.replace(' ','')
c+=len(b)
print(c)