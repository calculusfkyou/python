mod = 998244353

n,t = map(int, input().split())
x = [int(input()) for __ in range(n)]

ans = t + 1 - sum(x)
ps = n + ans

for i in range(n):
    ps += x[i] - 1
    ans = ans * ps % mod

print(ans * pow(t+1, mod-2, mod) % mod)