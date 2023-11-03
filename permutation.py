# python中的排列函式
from itertools import permutations

# 输入大写英文字母串
input_str = input("请输入大写英文字母串: ")

# 使用permutations函数生成排列
permutations_list = permutations(input_str)

# 打印排列
for perm in permutations_list:
    print(''.join(perm))


# 另一寫法
def get_permutations(s, current=""):
    if not s:
        print(current)
    else:
        for i in range(len(s)):
            remaining = s[:i] + s[i + 1:]
            get_permutations(remaining, current + s[i])


# 输入一个字符串
input_string = input("请输入一个字符串：")
get_permutations(input_string)
