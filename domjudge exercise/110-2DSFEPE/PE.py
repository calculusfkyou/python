def hanoi(n,a,b,c):
    if n==1:
        # print("A to C")
        return 1
    else:
        count=0
        count+=hanoi(n-1,a,c,b)
        # print("A to C")
        count+=1
        count+=hanoi(n-1,b,a,c)
        return count
while True:
    try:
        m=int(input())
        n=int(input())
        a,b,c=[],[],[]
        print(hanoi(n,a,b,c)*m)
    except EOFError:
        break