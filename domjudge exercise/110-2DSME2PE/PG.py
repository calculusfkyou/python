while True:
    try:
        temp=[]
        N=int(input())
        if N==0:
            break
        for i in range(N):
            no,weight,speed,decibel =map(float,input().split())
            temp.append([int(no),weight,speed,decibel])
        for k in range(N):
            temp[k].reverse()
        temp.sort(reverse =True)
        for i in range(N-1):
            if temp[i][0]==temp[i+1][0] and temp[i][1]==temp[i+1][1]:
                if temp[i][2]>=temp[i+1][2]:
                    for k in range(4):
                        temp[i][k],temp[i+1][k]=temp[i+1][k],temp[i][k]
                    if i!=0:
                        for j in range(i,0,-1):
                            if temp[i][0]==temp[i-1][0] and temp[i][1]==temp[i-1][1]:
                                if temp[i][2]<=temp[i-1][2]:
                                    for k in range(4):
                                        temp[i][k],temp[i-1][k]=temp[i-1][k],temp[i][k]
        for i in range(N):
            if i == N-1:
                print(temp[i][3])
            else:
                print(temp[i][3], end=' ')
    except EOFError:
        break