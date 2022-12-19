while True:
    N=int(input())
    for i in range(N):
        num=list(map(int,input().split()))
        stack=[]
        origin,temp,temp2=[],[],[]
        for j in range(len(num)):
            origin.append(num[j])
            temp.append(num[j])
        origin.sort()
        temp.sort()
        n=0
        for b in temp:
            m=0
            if b != num[n]:
                stack.append(b)
                break
        for k in temp:
            m=0
            if k != num[n] and num[n]!=stack[-1]:
                m=origin.index(k)
                stack.append(k)
                origin.pop(m)
            elif k == num[n] and num[n]==stack[-1]:
                temp2.append(stack[-1])
                n+=1
            elif k != num[n] and num[n]==stack[-1]:
                temp2.append(stack[-1])
                stack.pop(-1)
                n+=1
            else: 
                temp2.append(k)
                n+=1
        if temp2[-1]!=origin[-1]:
            for k in range(len(origin)):
                if temp2[k]!=origin[k]:
                    temp2.append(origin[k])
        if len(stack)!=0:
            stack.reverse()
            for h in range(len(stack)-1):
                temp2.append(stack[h])
        for a in range(len(num)):
            count=0
            if temp2[a]!=num[a]:
                print("no")
                count+=1
                break
        if count==0:
            print("yes")
        #3 4 5 6 7 2 1 8 9