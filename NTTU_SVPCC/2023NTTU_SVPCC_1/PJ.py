while True:
    try:
        n=int(input())
        rowgrid=[]
        for i in range(n):
            line=input()    
            rowgrid.append(line)
        columngrid=[]
        for i in range(len(rowgrid)):
            temp=""
            for j in range(len(rowgrid)):
                temp+=rowgrid[j][i]
            columngrid.append(temp)
        rowcheck,columncheck=0,0
        Bcount,Wcount=0,0
        for i in range(n):    
            if "BBB" in rowgrid[i] or "WWW" in rowgrid[i]:
                break
            Bc=rowgrid[i].count("B")
            Wc=rowgrid[i].count("W")
            if Bc==Wc:
                Bcount+=1
                Wcount+=1
        if Bcount==n and Wcount==n:
            rowcheck=1
        Bcount,Wcount=0,0
        for i in range(n):    
            if "BBB" in columngrid[i] or "WWW" in columngrid[i]:
                break
            Bc=columngrid[i].count("B")
            Wc=columngrid[i].count("W")
            if Bc==Wc:
                Bcount+=1
                Wcount+=1
        if Bcount==n and Wcount==n:
            columncheck=1
        if columncheck==1 and rowcheck==1:
            print(1)
        else:
            print(0)
    except EOFError:
        break