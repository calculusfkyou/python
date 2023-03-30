# def binarysearch(subtemp,key,left,right,count):
#     if left<=right:
#         mid=(left+right)//2
#         print(mid)
#         if key==subtemp[mid]:
#             #count+=1
#             return count
#         elif key<subtemp[mid]:
#             #count+=1
#             return binarysearch(subtemp,key,left,mid-1,count+1)
#         elif key>subtemp[mid]:
#             #count+=1
#             return binarysearch(subtemp,key,mid+1,right,count+1)
#     else:
#         return -1
        
# while True:
#     try:
#         M,N=map(int,input().split())
#         K=int(input())
#         if K<M or K>N:
#             print(-1)
#         else:
#             temp=[]
#             for i in range(M,N+1):
#                 temp.append(i)
#             print(binarysearch(temp,K,M,N,1))
#     except EOFError:
#         break

def binarysearch(key,left,right,count):
    if left<=right:
        mid=(left+right)//2
        if key==mid:
            #count+=1
            return count
        elif key<mid:
            #count+=1
            return binarysearch(key,left,mid,count+1)
        elif key>mid:
            #count+=1
            return binarysearch(key,mid,right,count+1)
    else:
        return -1
        
while True:
    try:
        M,N=map(int,input().split())
        K=int(input())
        if K<M or K>N:
            print(-1)
        else:
            # temp=[]
            # for i in range(M,N+1):
            #     temp.append(i)
            print(binarysearch(K,M,N,1))
    except EOFError:
        break