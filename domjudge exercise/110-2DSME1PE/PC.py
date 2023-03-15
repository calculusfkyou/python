import math
while True:
    try:
        n=int(input())
        if n==0:
            break
        val=list(map(int,input().split()))
        val.sort()
        # temp=0
        # for i in range(0,len(val)):
        #     temp+=val[i]  #總數量
        group=n//2
        print(group)  #能有幾組
        # single=val[0]+val[-1]  #一組有多少
        # for i in range(int(group)-1):
        #     print(single,end=" ")
        # print(single)
        for i in range(group):
            #print("%d %d"%(val[i],val[n-i-1]))
            if i+1==group:
                print(val[i]+val[n-i-1])
            else:
                print(val[i]+val[n-i-1],end=" ")
    except EOFError:
        break