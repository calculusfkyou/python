while True:
    try:
        tree=list(input())
        for i in range(len(tree)-1):
            try:
                if tree[i]==" ":
                    tree.pop(i)
            except:
                break
        No=[]#存英文字母的位置
        for i in range(len(tree)):
            if tree[i]!="0":
                temp=tree.index(tree[i])
                No.append(temp+1)#root為編號1
        newtree=[[0],[0]]
        path=1
        for i in range(1,len(tree)):
            if path==1:
                path=0
            else:
                path=1
            newtree.append([tree[i],path])
        alpha=[]
        for i in range(len(No)):#每個字母的數字
            temp=[]
            temp.append(newtree[No[i]][0])
            temp.append(newtree[No[i]][1])
            subi=No[i]//2
            while subi>1:
                temp.append(newtree[subi][1])
                subi=subi//2
            temp.reverse()
            n=""
            temp2=temp[:]
            for j in range(len(temp2)):
                if temp2[j]==0 or temp2[j]==1:
                    n+=str(temp2[j])
                    temp.pop(0)
            temp.append(n)
            temp.reverse()
            alpha.append(temp)
        
        M=int(input())
        for i in range(M):
            val=input()
            ans=""
            if val.isalpha():#都英文字母
                for j in range(len(val)):
                    for k in range(len(alpha)):
                        if val[j]==alpha[k][1]:
                            ans+=alpha[k][0]
                            break
            else:#都數字
                temp=""
                for j in range(len(val)):
                    temp+=val[j]
                    for k in range(len(alpha)):
                        if temp==alpha[k][0]:
                            ans+=alpha[k][1]
                            temp=""
                            break
            print(ans)
    except EOFError:
        break