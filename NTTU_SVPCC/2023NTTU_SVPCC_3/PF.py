def find_power_of_two(num):
    power=0
    while num>1:
        num=num/2
        power+=1
    return power
def copyfield(t,field):
    n1,n2=0,0
    for j in range(3):
        for i in range(len(field)):
            n1=field[i][0]
            n2=field[i][1]
            t.append([n1,n2])
    return t
def copy(temp2,t,cp):
    n1,n2=0,0
    for i in range(cp):
        n1=t[i][0]
        n2=t[i][1]
        temp2.append([n1,n2])
    temp2.reverse()
    return temp2
while True:
    try:
        n,k=map(int,input().split())
        field=[[1,1],[1,2],[2,2],[2,1]]
        if n==1:
            print(*field[k-1])
        else:
            subn=4  #處理長度
            tempn=4 #處理dis
            p=subn//2   
            cp=subn*subn//4
            t=[]
            for l in range(find_power_of_two(n)-1):
                dis=[]
                count=tempn-1
                disp=tempn//4
                # print(count)
                # print("--------------")
                while count!=3:
                    for i in range(disp):
                        dis.append(count)
                    count-=2
                dis.append(3)
                dis.append(1)
                dis.append(1)
                dis.append(3)
                if n>4:
                    redis=dis[:]
                    redis.reverse()
                    dis+=redis
                # print(dis)
                # print("--------------")
                t=copyfield(t,field)
                for i in range(4):
                    if i==0:
                        for j in range(0,(subn//2)**2):
                            t[j].reverse()
                    elif i==1:
                        for j in range((subn//2)**2,(subn//2)**2*2): 
                            t[j][1]+=p
                    elif i==2:
                        for j in range((subn//2)**2*2,(subn//2)**2*3):
                            t[j][0]+=p
                            t[j][1]+=p
                    else:
                        temp2=[]
                        temp2=copy(temp2,t,cp)
                        print(dis)
                        print("--------------")
                        print(temp2)
                        print("--------------")
                        for j in range(len(temp2)):
                            temp2[j][0]+=dis[j]
                            n1=temp2[j][0]
                            n2=temp2[j][1]
                            t.append([n1,n2])
                field.clear()
                field=copyfield(field,t)
                subn*=2
                tempn*=2
                p=subn//2
                cp=subn*subn//4
                print(t)
                print("--------------")
            # print(t)
            print(*field[k-1])
    except EOFError:
        break