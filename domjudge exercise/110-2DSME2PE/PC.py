def bbsort(subnum,n):
	for k in range(n):
		for j in range(0,len(subnum)-1):
			if subnum[j]>subnum[j+1]:
				temp=subnum[j+1]
				subnum[j+1]=subnum[j]
				subnum[j]=temp
	return subnum

def insertsort(subnum,n):
	for i in range(1,n-1):
		key=subnum[i]
		subi=i
		while key<subnum[subi-1] and subi!=0:
			temp=subnum[subi]
			subnum[subi]=subnum[subi-1]
			subnum[subi-1]=subnum[subi]
			subi-=1
	return subnum
			
def selectsort(subnum,n):
	for i in range(n):
		subi=i
		for k in range(i+1,len(subnum)+1):
			if subnum[k]<subnum[subi]:
				subi=k
			if subi!=k:
				temp=subnum[i]
				subnum[i]=subnum[subi]
	return subnum
    
while True:
    try:
        M,N=list(map(int,input().split()))
        nums=input().split()
        for i in range(1,N+1):
            print(i)
            print(insertsort(nums,i))
            print(bbsort(nums,i))
            print(selectsort(nums,i))
    except EOFError:
        break