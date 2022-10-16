"""
串列(list):
串列名稱 = [ 元素1, 元素2,...]
串列中各個元素資料型態可以相同，也可以不同， ex:
list = [1,2,3,4,5]               #元素皆為整數
list = ["香蕉", "蘋果", "橘子"]   #元素皆為字串
list = [1, "香蕉", True]         #包含不同資料型態元素
list[]                           #空串列

多維串列宣告:
list=[["joe","1234],["mary","abcd"],["david","5678"]]
print(list[1])    #["mary","abcd"]
print(list[1][1]) #abcd

讀取串列元素:
list = [1, 2, 3, 4, 5]
print(list[0])   #1
print(list[5])   #錯誤，索引值超過範圍
print(list[-1])  #1(倒數第一個)
print(list[-6])  #錯誤，索引值超過範圍
EXERCISE:
names = ["林小虎","王中森","邵木淼"] 
print(names[-1])
print(names[-2])

改變串列元素:
串列名稱[索引]=元素內容
list = [1,2,3,4,5]
print(list[0])  #1
list[0] = 9     #更改為9
print(list[0])  #9

for迴圈讀取串列:
for 變數 in 串列:
    程式區塊
ex:
list = ["香蕉", "蘋果", "橘子"]
for s in list:
    print(s, end=",")    #執行結果為:香蕉,蘋果,橘子,

取得串列長度:
scores=[1,2,3]
print(len(scores))   #3

for...range迴圈讀取串列:
score=[1,2,3]
for i in range(len(score)):    #即 for i in range(3)
    print(score[i])

串列搜尋與計次:
    index()搜尋(第幾個):
    索引值 = 串列名稱.index(串列元素)
    list = ["香蕉","蘋果","橘子"]
    n = list.index("蘋果")    #n=1
    m = list.index("梨子")    #ValueError: "梨子" is not on list

    count()計算次數(出現次數):
    次數=串列名稱.count(串列元素)
    list = ["香蕉","蘋果","橘子"]
    n = list.count("橘子")    #n=1
    m = list.count("梨子")    #m=0

串列元素新增和刪除:
串列名稱.append(元素值)   #append()是將元素加在串列最後面
ex:
list = [1,2,3,4,5,6]
list.append(7)
print(list[6])        #7
print(len(list))      #7

串列名稱.insert(索引值,串列元素)   #insert()將元素插入在串列中指定索引位置
ex:
list = [1,2,3,4,5,6]
list.insert(3,0)   #list = [1,2,3,0,4,5,6]
print(list[3])     #0
print(len(list))   #7
EXERCISE:
total = []
day = 1
deposit = sum = 0
while (day <= 7):
    deposit = int(input("請輸入第%d天的存款"%(day)))
    day += 1
    total.append(deposit)
for i in total:
    sum += i
print("存款總和:%d元"%(sum))

刪除串列元素:
串列名稱.remove(串列元素)    #remove()是刪除串列中第一個指定的串列元素，若串列元素不再串列中，醬會發生錯誤。
ex:
list = [1,2,3,4]
list.remove(2)
print(list)   #[1, 3, 4]

串列名稱.pop([index])       #pop()由串列中取出元素，同時傳列會將該元素移除。pop()可以有參數也可以沒有:若沒有參數，會取出最後一個元素;如果有，參數的資料型態必須為整數，就會取出以參數為索引值的元素。
ex:
list = [1,2,3,4,5,6]
n = list.pop()    #n=6, list=[1,2,3,4,5]
n = list.pop(2)   #n=3, list=[1,2,4,5]

del 可以刪除變數、串列，也可刪除串列元素。
del 串列名稱(n1)    #del 刪除串列單一元素。

刪除串列中索引第n1的元素，索引值也可以是負值，表示由串列的最後向前推算，若索引超出範圍，將發生錯誤。
del 串列名稱(n1:n2[:n3])    #del 刪除串列指定範圍元素，刪除索列中第n1到n2 - 1 的元素，間隔值為 n3 ,省略n3時預設值為1。
ex:
list1=[1,2,3,4,5,6]
del list1(1)
print(list1)    #[1,3,4,5,6]
list2=[1,2,3,4,5,6]
del list2[1:5:2]   #刪除索引第1、3的串列元素
print(list2)    #[1,3,5,6]
EXERCISE:
colors = ['紅', '橙', '黃', '綠', '藍']
while True:
    color = input("請輸入要刪除的顏色(Enter 結束):")
    if color == "":
        break
    n = colors.count(color)
    if n > 0:
        colors.remove(color)
    print("顏色有:",colors)

串列排序:
串列名稱.sort()    #sort()將指定的串列由小到大排序
ex:
list=[3,2,1,5]
list.sort()
print(list)    #[1,2,3,5]

串列名稱.reverse()    #reverse()將指定的串列反轉
ex:
list=[3,2,1,5]
list.reverse()
print(list)         #[5,1,2,3]

串列名稱2 = sorted(串列名稱1,reverse=True)    #sorted(將指定的串列排序) 
#串列名稱1代表要排序的串列，串列名稱2代表排序後的另一個串列。 reverse可以設定順序，True由大到小排序，False則又小到大排序，省略時預設為False。
ex:
list1=[3,2,1,5]
list2=sorted(list1,reverse=True)     #將list1的值傳入list2並排序
print(list2)          #[5,3,2,1]
print(list1)          #[3,2,1,5]  #原串列不變
EXERCISE:
grades = []
while True:
    grade = input("請輸入學生的成績:")
    if grade == "":
        break
    grades.append(int(grade))
grades2 = sorted(grades,reverse=False)
print(grades2)

元組(Tuple)
元組名稱 = (元素1,元素2,...)
元組使用方式和串列相同，但不能修改元素值，否則會發生錯誤。   
串列的進階方法也可用於元組，但因為不能修改元素值，所以會蓋=改變元素個數或元素值的方法都不能在元組中使用，ex:append、insert等方法。
元組比較串列的好處:執行速度較快，存取元組的資料較為安全

EXERCISE:
numbers = [21,4,35,1,8,7,3,6,9]
odd_numbers = []
for i in numbers:
    if i % 2 != 0:
        odd_numbers.append(i)
print(odd_numbers)
"""
fruits = ["香蕉","蘋果","橘子","鳳梨","西瓜"]
while True:
    fruit = input("請輸入喜歡的水果(Enter 結束):")        
    m = fruits.count(fruit)
    if fruit == "":
        break
    elif m == 0:
        print("%s不在串列中!"%(str(fruit)))
    elif m != 0:
        n = fruits.index(fruit)
        # print("%s在串列中的第%d項"%(str(fruit),n+1))
        print("在串列中的第"+ str(n+1) +"項")

