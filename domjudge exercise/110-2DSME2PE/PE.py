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
        for j in range(1,l+1):#長度的因數有幾個
            if l%j==0:
                count+=1
        if count>2:
            for i in range(1,l+1):
                if l%i==0:  #i為因數時
                    for k in range(0,l,i):
                        temp.append(s[k:k+i])
                    temp.sort() #依照ascii排
                    for j in temp:
                        t+=j
                    temp.clear()
                    if t!=s:
                        print(t)
                    t=''
        else:#長度為質數，不會產出新字串
            print("orz")
    except EOFError:
        break