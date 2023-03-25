while True:
    try:
        N,K=map(int,input().split())
        level=list(map(int,input().split()))
        level.sort()
        
    except EOFError:
        break