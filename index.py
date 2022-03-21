import sys
test = int(input())
for t in range(test):
    b = list(map(int, sys.stdin.readline().split()))
    avg = 0
    for b1 in range(1,len(b)):
        avg += b[b1]
    avg /= b[0]
    n = 0
    for b1 in range(1,len(b)):
        if b[b1]>avg:
            n+=1
    print("{:.3f}%".format(n/b[0]*100))