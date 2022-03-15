import sys

a,b = map(int,sys.stdin.readline().split(" "))
c = sys.stdin.readline().split(" ")

for d in c:
    if int(d)<b:
        print(d, end = " ")
print(type(a))