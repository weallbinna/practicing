for re in range(int(input())):
    even = int(input())
    lst = [True]*(even+1)
    for index in range(2,int(even**0.5+1)):
        if lst[index]:
            for index1 in range(2*index,even+1,index):
                lst[index1] = False
    for prime in range(even//2,even):
        if lst[prime]:
            if lst[even-prime]:
                print(even-prime,prime)
                break