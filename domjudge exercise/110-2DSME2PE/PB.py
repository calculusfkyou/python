while True:
    try:
        m,n=map(int,input().split())
        p=input().split()
        e=input().split()
        p.sort()
        count=0
        for i in e:
            for k in p:
                if k>=i:
                    count+=int(k)
                    break
        print(count)
    except EOFError:
        break   