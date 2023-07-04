while True:
    try:
        n=int(input())
        ans,bs=0,0
        temp=[]
        while n>0:
            modn=n%10
            for i in range(1,10):
                if (i**2)%10==modn:
                    temp.append(i)
            n=n//10
    except EOFError:
        break