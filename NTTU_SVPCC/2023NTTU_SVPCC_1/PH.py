def main():
    while True:
        try:
            n,m=map(int,input().split())
            path,npath=[],[]
            for i in range(m):
                path.append(list(map(int,input().split())))
            if n==2:
                print(0)
            else:
                for i in range(len(path)):
                    if path[0][0]==1:
                        npath.append(path[0])
                        path.pop(0)
                    else:
                        break
                completepath=[]
                check=1
                while check:
                    for i in range(len(npath)):
                        temp=npath[i][-1]
                        if temp==n:
                            completepath.append(npath[i])
                        else:
                            for j in range(len(path)):
                                sub=[]
                                if path[j][0]==temp:
                                    sub=npath[i]+path[j]
                                    sub.pop(-2)
                                    completepath.append(sub)
                                    if path[j][1]==n:
                                        check=0
                    npath=completepath[:]
                    completepath.clear()
                # print(npath)
                shortestlen=len(npath[0])
                for i in range(len(npath)):
                    if len(npath[i])<=shortestlen:
                        shortestlen=len(npath[i])
                print(shortestlen-2)
        except EOFError:
            break
main()
#7 8
# 1 2
# 1 3
# 2 4
# 3 4
# 4 5
# 4 6
# 5 7
# 6 7