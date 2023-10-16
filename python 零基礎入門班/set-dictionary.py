# 集合的運算
# s1={3,4,5}
# print(3 in s1)
# print(10 not in s1)
# s1={3,4,5}
# s2={4,5,6,7}
# s3=s1&s2 # &表交集(取相同資料)
# s3=s1|s2  # |表聯集(取集合中所有資料，但不重複取)
# s3=s1-s2  # - 表差集(從s1中減去和s2重疊的部分)
# s3=s1^s2  # ^表反交集(取兩集合中，不重疊的部分)
# print(s3)
# s=set("Hello") # 把字串中的字母拆解成集合: set(字串)
# print("H" in s)

# 字典的運算: key-value 配對
# dic={"apple":"蘋果","bug":"蟲蟲"}
# (基操) #dic["apple"]="小蘋果"  #print(dic["apple"])
# print("apple" in dic)
# print("banana" not in dic)#判斷key是否存在
# print(dic)
# del dic["apple"] # 刪除字典中的鍵值對 (key-value pair)
# print(dic)
dic = {x: x * 2 for x in [3, 4, 5]}  # 從列表的資料產生字典
print(dic)

"""------看以下就好------"""
"""
集合常用函式 (集合是大括號)
set.add(element): 向集合添加一個元素。
set.update(iterable): 將多個元素添加到集合中。
set.remove(element): 從集合中刪除指定的元素。如果元素不存在，會引發KeyError。
set.discard(element): 從集合中刪除指定的元素。如果元素不存在，不會報錯。
set.pop(): 移除並返回集合中的任意一個元素。如果集合為空，會引發KeyError。
set.clear(): 清空集合，使其不包含任何元素。
set.copy(): 複製一個集合
set1.union(set2): 返回兩個集合的聯集
set1.intersection(set2): 返回兩個集合的交集
set1.difference(set2): 返回包含在第一個集合中但不在第二個集合中的元素的新集合。
set1.issubset(set2): 檢查一個集合是否是另一個集合的子集
set1.issuperset(set2): 檢查一個集合是否是另一個集合的超集
"""

"""
字典常用函式 (字典是大括號)
dict.get(key, default)：獲取字典中鍵對應的值。如果鍵不存在，返回預設值。
dict1.update(dict2)：將一個字典的鍵-值對添加到另一個字典中。
dict.pop(key, default)：移除字典中給定鍵的鍵值對，如果鍵不存在，返回默認值或引發KeyError。
dict.popitem()：隨機移除字典中的一個項目，並以元組形式返回。
dict.clear()：移除字典中的所有項目，使字典變為空字典。
dict.keys()：返回字典中所有的鍵。
dict.values()：返回字典中所有的值。
dict.items()：返回字典中所有的鍵-值對。
in 運算子：用於檢查鍵是否存在於字典中。
    my_dict = {"蘋果": 3, "香蕉": 2}
    if "蘋果" in my_dict:
        print("蘋果存在")
"""
