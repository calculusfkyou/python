def countAndSay(n):
    if n == 0:
        return "1"
    if n == 1:
        return "11"
    s = countAndSay(n-1)
    count = 1
    res = ""
    for i in range(len(s)):
        if i == len(s) - 1 or s[i] != s[i+1]:
            res += str(count) + s[i]
            count = 1
        else:
            count += 1
    return res

while True:
    try:
        x = int(input())
        if x==-1:
            break
        print(countAndSay(x))
    except EOFError:
        break