import random as r

# random.random() 返回一個位於0.0（包含）到1.0（不包含）之間的隨機浮點數。
print(r.random())

# random.randint(a, b) 返回一個位於a（包含）和b（包含）之間的隨機整數。
# 擲骰子遊戲
print(r.randint(1, 6))

# random.uniform(a, b) 返回一個位於a（包含）和b（包含）之間的隨機浮點數。
print(r.uniform(1, 10))

# random.choice(seq) 從序列seq中隨機選擇一個元素並返回。
# 擲骰子遊戲
s, ss = "123456", [1, 2, 3, 4, 5, 6]
print(r.choice(s), r.choice(ss))

# random.sample(population, k) 從population中隨機選擇k個獨立的元素，並返回一個包含這些元素的列表。
print(r.sample(s, 3), r.sample(ss, 3))

# random.randrange ([start,] stop [,step]) 返回一個位於start（包含）和stop（不包含）之間，且以step為步長的隨機整數。 (step預設為1)
print(r.randrange(100, 1000, 2))
print(r.randrange(100, 1000, 3))  # 需-100後才是3的倍數，也就是說以start為起點，遞增取值。

# random.shuffle(x) 隨機打亂列表x中的元素的順序，並不返回新的列表。
List = [1, 2, 3, 4, 5, 6]
r.shuffle(List)
print(List)
