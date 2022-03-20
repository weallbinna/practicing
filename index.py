num = int(input())
for n in range(num):
    score = 0
    s = 0
    result = input()
    for a in range(len(result)):
        if result[a] == "O":
            s+=1
            score += s
        else:
            s = 0
    print(score)