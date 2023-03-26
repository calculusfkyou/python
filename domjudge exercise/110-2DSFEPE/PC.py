#import statistics
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
                if len(temp)==1:
                    total+=j
                else:
                    temp.sort()
                    if len(temp)%2!=0:
                        total+=temp[len(temp)//2]
                    else:
                        total+=int((temp[len(temp)//2]+temp[(len(temp)-1)//2])/2)
                # total+=int(statistics.median(temp))
            temp.clear()
            print(total)
    except EOFError:
        break