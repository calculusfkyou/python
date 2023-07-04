while True:
    try:
        m=int(input())
        weight=[]
        for i in range(m):
            weight.append(int(input()))
        weight.sort()
        max=weight[-1]
        target=0
        temp=weight.count(max)
        if temp==len(weight):
            target=max
            print(target)
        else:
            while len(weight)!=1:
                target,sum=0,0
                while len(weight)>1:
                    if sum!=0:
                        target=weight[0]+1
                    else:
                        target=weight[0]
                    if sum>=max:
                        break
                    else:
                        sum+=weight[0]
                        weight.pop(0)   
            print(target)
    except EOFError:
        break