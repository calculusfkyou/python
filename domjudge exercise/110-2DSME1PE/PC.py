while True:
    n=int(input())
    val=list(map(int,input().split()))
    temp=0
    for i in range(0,len(val)):
        temp+=val[i]
    if n==0:
        break
    group=n/2
    if group%1>0:
        print(int(group))
        while(temp>int(group)):
            print(temp/int(group),end=" ")
            temp/=int(group)
        