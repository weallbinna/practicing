a = input()
b = list(range(65,91))
b1 = list(range(97,123))
d = []
d1 = []
f = []
for c in b :
    d.append(a.count(chr(c)))
for c in b1:
    d1.append(a.count(chr(c)))
for c in range(len(b)):
    f.append(d[c]+d1[c])
if f.count(max(f))>1:
    print("?")
else:
    print(chr(b[f.index(max(f))]))

# g = input().upper()

# h = list(set(g))
# f = []
# for i in h:
#     f.append(g.count(i))
# if f.count(max(f))>1:
#     print('?')
# else:
#     print(h[f.index(max(f))])