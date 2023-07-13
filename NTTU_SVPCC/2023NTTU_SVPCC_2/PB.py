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
    return n
while True:
    try:
        m,n=map(int, input().split())
        print(math.gcd(m,n))
        # print(gcd(m,n))
    except EOFError:
        break
