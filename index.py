a,b,c = map(int,input().split(" "))

if a==b==c:
    print(10000+a*1000)
elif a==b!=c or a==c!=b or b==c!=a:
    if a==b!=c:
        print(1000+a*100)
    elif a==c!=b:
        print(1000+a*100)
    elif b==c!=a:
        print(1000+b*100)
else:
    if a>b and a>c:
        print(a*100)
    elif b>a and b>c:
        print(b*100)
    elif c>a and c>b:
        print(c*100)
       
# better code
# a,b,c = list(map(int, input().split()))

# lst = [a,b,c]
# s = list(set(lst))
# n = len(s)

# if n ==1 :
#     print(10000+a * 1000)
# elif n ==2 :
#     lst.remove(s[0])
#     lst.remove(s[1])
#     print(1000+ lst[0]*100)
# else:
#     print(max(lst)*100)