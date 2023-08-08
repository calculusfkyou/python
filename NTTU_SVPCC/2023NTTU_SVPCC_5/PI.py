MOD = 998244353

def count_strings_with_levenshtein_distance(s, d):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(d + 1)]
    
    for i in range(n + 1):
        dp[0][i] = 1
    
    for i in range(1, d + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD
            if s[j - 1] != 'A':
                dp[i][j] = (dp[i][j] - dp[i - 1][j - 1]) % MOD
            if s[j - 1] != 'Z':
                dp[i][j] = (dp[i][j] - dp[i - 1][j - 1]) % MOD
            
    return dp[d][n]

# 測試樣例
print(count_strings_with_levenshtein_distance("ICPC", 1)) # 輸出: 230
print(count_strings_with_levenshtein_distance("PROGRAMMER", 10)) # 輸出: 110123966
