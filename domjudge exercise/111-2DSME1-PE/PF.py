case=1
while True:
    try:
        n=int(input())
        if n<100:
            print("Case %d: %d"%(case,n))
            case+=1
        else:
            temp=[]
            while n>0:
                try:
                    temp2=n%100
                    if temp2!=0:
                        temp.append(temp2)
                    n=n//100
                    if n==0:
                        break

                    temp2=n%10
                    if temp2!=0:
                        temp.append("hundred")
                        temp.append(temp2)
                    n=n//10
                    if n==0:
                        break

                    temp2=n%1000
                    if n<1000 and n!=0:
                            temp.append(n%100)
                            temp.append("hundred")
                            if n<100:
                                temp.append(n//100)
                            break
                    if temp2!=0:
                        temp.append("thousand")
                        temp.append(temp2)
                    n=n//1000
                    if n==0:
                        break

                    temp2=n%1000
                    if n<1000 and n!=0:
                            temp.append(n%100)
                            temp.append("hundred")
                            if n<100:
                                temp.append(n//100)
                            break
                    if temp2!=0:
                        temp.append("million")
                        temp.append(temp2)
                    n=n//1000
                    if n==0:
                        break

                    temp2=n%1000
                    if n<1000 and n!=0:
                            temp.append(n%100)
                            temp.append("hundred")
                            if n<100:
                                temp.append(n//100)
                            break
                    if temp2!=0:
                        temp.append("billion")
                        temp.append(temp2)
                    n=n//1000
                    if n==0:
                        break

                    if n!=0:
                        temp.append("trillion")
                except:
                    break
            temp.reverse()
            print("Case %d: "%(case),end="")
            case+=1
            for i in range(len(temp)-1):
                print(temp[i],end=" ")
            print(temp[-1])
    except EOFError:
        break