temp=[1,1]
ans=[1]
while True:
    try:
        n=int(input())
        if n==0:
            print(1)
            print(1)
        elif n==1:
            print("1 1")
            print(2)
        else:
            temp=[1,1]
            for i in range(0,n-1):
                for j in range(len(temp)-1):
                    ans.append(temp[j]+temp[j+1])
                ans.append(1)
                temp=ans[:]
                ans=[1]

            for i in range(len(temp)-1):
                print(temp[i],end=" ")
            print(temp[-1])
            print(sum(temp))
    except:
        break