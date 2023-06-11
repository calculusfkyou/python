while True:
    try:
        n,r=map(int,input().split())
        val=list(map(int,input().split()))
        if n==r:
            print("*")
        else:
            temp=[]
            for i in range(1,n+1):
                if i not in val:
                    temp.append(i)
            for i in range(len(temp)-1):
                print(temp[i],end=" ")
            print(temp[-1])
    except EOFError:
        break