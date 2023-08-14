import random
while True:
    try:
        n=int(input())
        meals=[]
        for i in range(n):
            temp=list(input().split())
            temp[0]=int(temp[0])
            meals.append(temp)
        meals.sort(key=lambda meals:meals[0],reverse=1)
        ma=meals[0][0]
        remeals=[]
        for i in range(len(meals)):
            if meals[i][0]==ma:
                remeals.append(meals[i])
            else:
                break
        randommeal=random.choice(remeals)
        for i in randommeal:
            print(i)
    except EOFError:
        break