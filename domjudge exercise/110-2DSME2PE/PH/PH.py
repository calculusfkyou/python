#不知道錯哪裡
def main():
    while True:
        try:
            n,p=map(int,input().split())        
            h=list(map(int, input().split()))
            w=list(map(int, input().split()))
            if sum(w)==0:
                print(1)
            if sum(h)==0:
                print(0)
            else:
                height=[] #高度轉0和1
                ma=max(h)
                for i in range(len(h)):
                    t=h[i]
                    if t==0:
                        height.append([0])
                        for j in range(ma-1):
                            height[i].append(0)
                    else:
                        height.append([1])
                        for j in range(t-1):
                            height[i].append(1)
                        for j in range(ma-t):
                            height[i].append(0)
                ans=ma
                for i in range(len(w)):
                    temp=w[i]
                    check=0
                    subh=ans
                    for j in range(subh-1,-1,-1):#從第7行先找
                        for k in range(n):#有n列
                            if check==temp:
                                break
                            if check==1 and height[k][j]==0:
                                check=0
                            if height[k][j]==1:
                                height[k][j]=0
                                check+=1
                        if check==temp:
                            break
                        else:
                            ans-=1
                print(ans)
        except EOFError:
            break
main()