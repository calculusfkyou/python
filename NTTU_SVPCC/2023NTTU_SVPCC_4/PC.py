while True:
    try:
        w,h=map(int,input().split())
        print(w+h-(float(w**2+h**2))**0.5)
    except EOFError:
        break