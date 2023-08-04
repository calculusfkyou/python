import math

while True:
    try:
        w,h=map(int,input().split())
        if w+h-math.sqrt(w**2+h**2)-int(w+h-math.sqrt(w**2+h**2))!=0:
            print("%.9f"%(w+h-math.sqrt(w**2+h**2)))
        else:
            print("%d"%(w+h-math.sqrt(w**2+h**2)))
    except EOFError:
        break