import statistics
while True:
    try:
        temp=[]
        T=int(input())
        for i in range(T):
            total=0
            n=int(input())
            nums=list(map(int,input().split()))
            for j in nums:
                temp.append(j)
                total+=int(statistics.median(temp))
            temp.clear()
            print(total)
    except EOFError:
        break