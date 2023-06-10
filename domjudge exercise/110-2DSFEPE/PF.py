while True:
    try:
        N,K=map(int,input().split())
        level=list(map(int,input().split()))
        level.sort()
        #[等級,白,黑]
        for i in range(len(level)):
            if i==0:
                level.append([level[0],0,1])
            elif i==len(level)-1:
                level.append([level[0],1,0])
            else:
                level.append([level[0],0,0])
            level.pop(0)
        difference=[]#[玩家1,玩家2,差]
        for i in range(1,len(level)):
            for j in range(i,len(level)):
                difference.append([i-1,j,level[j][0]-level[i-1][0]])
        difference.sort(key=lambda difference:difference[2])
        sum=0
        for j in range(len(difference)):
            if K!=0:
                check,check2=1,0
                if level[difference[j][0]][1]!=1:#小
                    check=difference[j][0]
                if level[difference[j][1]][2]!=1:#大
                    check2=difference[j][1]
                if (check+1)==check2:
                    level[check][1]=1
                    level[check2][2]=1
                    sum+=level[check2][0]-level[check][0]
                    K-=1
            else:
                break
        print(sum)
    except EOFError:
        break
