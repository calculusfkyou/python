while True:
    try:
        s=input()
        l=len(s)
        temp=[]
        t=''
        if l==0:
            print("orz")
            break
        count=0
        for j in range(1,l+1):
            if l%j==0:
                count+=1
        if count>2:
            for i in range(1,l+1):
                if l%i==0:
                    for k in range(0,l,i):
                        temp.append(s[k:k+i])
                    temp.sort()
                    for j in temp:
                        t+=j
                    temp.clear()
                    if t!=s:
                        print(t)
                    t=''
        else:
            print("orz")
    except EOFError:
        break