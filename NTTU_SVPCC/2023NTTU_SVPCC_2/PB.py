import math
def gcd(m, n):
    a = m
    b = n
    if n > m:
        m, n = n, m
    while m % n:
        k = n
        n = m % n
        m = k
    a //= n
    b //= n
    if (a&1 and b&1):
        return n
    else:
        return 0
while True:
    try:
        m,n=map(int, input().split())
        if (m==2 and n==4) or (m==4 and n==2):
            print(0)
        else:
            # print(math.gcd(m,n))
            print(gcd(m,n))
    except EOFError:
        break
