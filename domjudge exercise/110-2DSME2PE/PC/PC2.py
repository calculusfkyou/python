def insertsort(subnum,n):
    if n==1:#第一次不變
        for i in range(len(subnum)-1):
            print(subnum[i],end=" ")
        print(subnum[-1])
        return None
    for i in range(n-1,0,-1):#n-1 ~ 1
        if subnum[i]>subnum[i-1]:
            subnum[i],subnum[i-1]=subnum[i-1],subnum[i]
        else:
            break
    for i in range(len(subnum)-1):
        print(subnum[i],end=" ")
    print(subnum[-1])

def bbsort(subnum,n):
    for j in range(len(subnum)-1,0,-1):#從左邊把大的推過去
        if subnum[j]>subnum[j-1]:
            subnum[j],subnum[j-1]=subnum[j-1],subnum[j]
    for i in range(len(subnum)-1):
        print(subnum[i],end=" ")
    print(subnum[-1])

def selectsort(subnum,n):
    temp=[]
    ma=subnum.index(max(subnum))
    temp.append(subnum[ma])
    subnum[ma]=subnum[0]
    subnum.pop(0)
    return temp

while True:
    try:
        M,N=map(int,input().split())
        nums=list(map(int,input().split()))
        nums2=nums[:]
        nums3=nums[:]
        ss,ans=[],[]
        print(1)
        for i in range(1,N+1):
            insertsort(nums,i) 
        print(2)
        for i in range(1,N+1):
            bbsort(nums2,i)
        print(3)
        for i in range(1,N+1):
            ss+=selectsort(nums3,i)
            ans=ss+nums3
            for k in range(len(ans)-1):
                print(ans[k],end=" ")
            print(ans[-1])
    except EOFError:
        break