def changetowin(string):
    if string=="R":
        return "S"
    elif string=="S":
        return "P"
    elif string=="P":
        return "R"
while True:
    try:
        n,m=map(int,input().split())
        RPS=input()
        mine=input()
        possible=[]
        temp=""
    except:
        break