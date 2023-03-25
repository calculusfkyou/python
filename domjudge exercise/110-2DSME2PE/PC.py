#TRUE
def insertsort(subnum,n):
    if n==1:
        for i in range(len(subnum)-1):
            print(subnum[i],end=" ")
        print(subnum[-1])
        return None
    for i in range(1,n):
        for k in range(i,0,-1):
            if subnum[k]>subnum[k-1]:
                subnum[k],subnum[k-1]=subnum[k-1],subnum[k]
                i-=1
            else:
                break
    for i in range(len(subnum)-1):
        print(subnum[i],end=" ")
    print(subnum[-1])

#TRUE    
def bbsort(subnum,n):
    for j in range(len(subnum)-1,0,-1):
        if subnum[j]>subnum[j-1]:
            subnum[j],subnum[j-1]=subnum[j-1],subnum[j]
    for i in range(len(subnum)-1):
        print(subnum[i],end=" ")
    print(subnum[-1])

def selectsort(subnum,n):
    temp=[]
    l=len(subnum)
    for i in range(n):
        idx=subnum.index(max(subnum))
        subnum[0],subnum[idx]=subnum[idx],subnum[0]
        temp.append(subnum[0])
        subnum.pop(0)
    temp+=subnum
    return temp

while True:
    try:
        M,N=map(int,input().split())
        nums=list(map(int,input().split()))
        nums2=nums[:]
        nums3=nums[:]
        ss=[]
        print(1)
        for i in range(1,N+1):
            insertsort(nums,i)
        print(2)
        for i in range(1,N+1):
            bbsort(nums2,i)
        print(3)
        for i in range(1,N+1):
            ss=selectsort(nums3,i)
            for k in range(len(ss)-1):
                print(ss[k],end=" ")
            print(ss[-1])
            nums3=ss
    except EOFError:
        break