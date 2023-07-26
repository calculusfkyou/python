# 有序可變動列表 List
grades=[12,60,25,70,90]
print(grades)
print(grades[0])
print(grades[3])
print(grades[1:4])
# 把 55 放到列表中的第一個位置
grades=[12,60,25,70,90]
grades[0]=55 
print(grades)
# 連續刪除列表中從編號 1 到編號 4(不包括) 的資料
grades=[12,60,25,70,90]
grades[1:4]=[] 
print(grades)
# 列表增加更多資料
grades=[12,60,25,70,90]
grades=grades+[12,33]
print(grades)
# 取得列表的長度 len(列表資料)
grades=[12,60,25,70,90] 
length=len(grades)
print(length)
#列表中的列表  print(data[第幾個列表][列表中的資料])
data=[[3,4,5],[6,7,8]]
print(data[0])
print(data[0][1])
print(data[0][0:2])
print(data)
data[0][0:2]=[5,5,5]   #第一個列表中 3,4換成5,5,5
print(data)

# 有序不可變動列表 Tuple
data=(3,4,5)
data[0]=5  #錯誤︰Tuple的資料不可以變動
print(data[2])
print(data[0:2])
