while True:
    try:
        p,d=map(int,input().split())
        grid=[]
        total,Avote,Bvote=0,0,0
        temp=[]
        for i in range(p):
            arr=list(map(int,input().split()))
            total=total+arr[1]+arr[2]
            if i>0:
                if arr[0] in temp:
                    for j in range(len(grid)):
                        if arr[0]==grid[j][0]:
                            grid[j][1]+=arr[1]
                            grid[j][2]+=arr[2]
                else:
                    grid.append(arr)
            else:
                grid.append(arr)
            temp.append(arr[0])
        grid.sort(key=lambda grid:grid[0])
        for i in range(len(grid)):
            if grid[i][1]>grid[i][2]:
                print("A %d %d"%(grid[i][1]-((grid[i][1]+grid[i][2])//2+1),grid[i][2]))
                Avote+=grid[i][1]-((grid[i][1]+grid[i][2])//2+1)
                Bvote+=grid[i][2]
            else:
                print("B %d %d"%(grid[i][1],grid[i][2]-((grid[i][1]+grid[i][2])//2+1)))
                Avote+=grid[i][1]
                Bvote+=grid[i][2]-((grid[i][1]+grid[i][2])//2+1)
        print("%.10f"%(abs(Avote-Bvote)/total))
    except EOFError:
        break