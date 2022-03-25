S = input()
r = 'abcdefghijklmnopqrstuvwxyz'
for i in r:
    for a in range(len(S)):
        if i not in S:
            print("-1", end = " ")
            break
        if i == S[a]:
            print(a , end = " ")
            break