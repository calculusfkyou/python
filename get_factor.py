def get_factors(n):
    factors = []
    # 質因數分解
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    print(factors)
    # 求得所有因數
    num_factors = len(factors)
    all_factors = set()
    for i in range(1 << num_factors):
        factor = 1
        for j in range(num_factors):
            if (i >> j) & 1:
                factor *= factors[j]
        all_factors.add(factor)
    return sorted(all_factors)

if __name__ == "__main__":
    print(get_factors(10))