while True:
    try:
        n=int(input())
        char=list(input().split())
        val=list(input().split())
        temp=[]
        for i in range(len(val)):
            if val[i]!="+" and val[i]!="-" and val[i]!="*":
                temp.append(char[ord(val[i])-65])
            elif val[i]=="-":
                if temp[-1]=="T":
                    temp.append("F")
                else:
                    temp.append("T")
                temp.pop(-2)
            elif val[i]=="*" or val[i]=="+":
                if val[i]=="*":
                    if temp[-1]=="T" and temp[-2]=="T":
                        temp[-2]="T"
                    else:
                        temp[-2]="F"
                    temp.pop()
                else:
                    if temp[-1]=="F" and temp[-2]=="F":
                        temp[-2]="F"
                    else:
                        temp[-2]="T"
                    temp.pop()
        print(temp[0])
    except EOFError:
        break