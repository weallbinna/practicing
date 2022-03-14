import sys

a = int(sys.stdin.readline())

for d in range(1,a+1):
    a,b = map(int,sys.stdin.readline().split())
    print(f"Case #{d}: {a} + {b} = {a+b}")