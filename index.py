while True:
    cnt = 0
    nm = int(input())
    if nm == 0:
        break
    lst = [True]*(nm*2+1)
    for i in range(2, int(2*nm**0.5)+1):
        if lst[i]:
            for j in range(2*i, nm*2+1, i):
                lst[j] = False
    del lst[:nm+1]
    print(lst.count(True))