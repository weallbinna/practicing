def Selfnum(a):
        if  a<100:
            return a+a//10+a%10
        elif a>=100 and a<1000:
            b = a%100
            return a+a//100+b//10+b%10
        elif a>=1000 and a<10000:
            b = a%1000
            c = b%100
            return a+a//1000+b//100+c//10+c%10
S = []
for a in range(9973):
    S.append(Selfnum(a))
S.sort()
S = set(S)
all = [n for n in range(10003)]
for s in S:
    all.remove(s)
all.remove(10001)
for num in range(len(all)):
    print(all[num])