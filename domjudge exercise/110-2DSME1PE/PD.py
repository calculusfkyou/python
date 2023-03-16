while True:
    try:
        n=int(input())
        for i in range(n):
            k=int(input())
            names=list(input().split())
            while(len(names)!=1):
                names.append(names[0])
                names.append(names[1])
                names.pop(0)
                names.pop(0)
                names.pop(0)
            print(names[0])
    except EOFError:
        break