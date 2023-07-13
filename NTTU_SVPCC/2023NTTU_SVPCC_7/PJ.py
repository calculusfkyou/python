while True:
    try:
        c,e,m=map(int,input().split())
        ans=[]
        for i in range(2,m):
            if m%i==0:
                if e==(i+m//i)*2:
                    if (i+2)>(m//i+2):
                        ans.append([i+2,m//i+2])
                    else:
                        ans.append([m//i+2,i+2])
        if len(ans)==0:
            print('impossible')
        else:
            print(*ans[0])
    except EOFError:
        break