a,b = map(int,input().split(" "))
c = int(input())

if c>=60:
    d = c/60   
    e = c%60  
    a += d
    b += e
    if b >= 60:
        f = b%60
        g = b/60
        a += g
        b = f
    if a >= 24:
        a = a%24
        
elif c< 60:
    b += c
    if b>=60:
        g = b%60
        f = b/60
        a += f
        b = g
    if a >= 24:
        a = a%24

print(int(a),int(b))
        
        