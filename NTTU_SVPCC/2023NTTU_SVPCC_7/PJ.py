import random
def prime_factorization(n):
    factors=[]
    i=2
    while i*i<=n:
        if n%i:
            i+=1
        else:
            n//=i
            factors.append(i)
    if n>1:
        factors.append(n)
    return factors
def get_factors(n):
    factors=[]
    # 質因數分解
    for i in range(2,int(n**0.5)+1):
        while n%i==0:
            factors.append(i)
            n//=i
    if n>1:
        factors.append(n)
    # print(factors)
    # 求得所有因數
    num_factors=len(factors)
    all_factors=set()
    for i in range(1<<num_factors):
        factor=1
        for j in range(num_factors):
            if (i>>j)&1:
                factor*=factors[j]
        all_factors.add(factor)
    return sorted(all_factors)
def main():
    while True:
        try:
            c,e,m=map(int,input().split())
            ans=[]
            temp=get_factors(m)
            for i in range(len(temp)):  
                t=m//temp[i]
                if e==(t+temp[i])*2:
                    ans.append([t+2,temp[i]+2])
            print(ans)
            if len(ans)==0:
                print('impossible')
            else:
                print(*random.choice(ans))
        except EOFError:
            break
main()