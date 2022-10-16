"""
range函式使用1個參數的語法為:
數列變數 = range(整數值)
list = range(5)  #數列為0,1,2,3,4

range函式使用2個參數的語法為:
數列變數 = range (起始值, 終止值)
list = range (-2, 4) #數列為-2, -1, 0, 1, 2, 3

range函式使用3個參數的語法為:
數列變數 = range (起始值, 終止值, 間隔值)
list = range (3, 8, 1) #數列為3, 4, 5, 6, 7
list = range (3, 8, 2) #數列為3, 5, 7

for迴圈:
#for 變數 in 數列:
    程式區塊
#for 變數 in (起始值, 終止值, 間隔值):
    程式區塊
for n in range(3):
    print(n, end=",")  #結果為:0,1,2
EXERCISE:
n = int(input("請輸入正整數:"))
for i in range(1, n+1, 2):
    print(i,end=" ")

n =int(input("請輸入正整數:"))
for i in range(1, n, 2):
    print(i,end=" ")

巢狀for迴圈:
EXAMPLE:
for i in range(1,6):  #外部迴圈, 共執行五次
    print("外部第",i,"次迴圈,內部執行",i,"次迴圈", end="")
    for j in range(1,i+1):    #內部迴圈
        print("#", end="")
    print()    #換行
EXERCISE:利用兩層for迴圈列印99乘法表
for i in range(1, 10):
    print()
    for j in range(1, 10):
        print('%d*%d=%d'%(i,j,i*j),end=" ")

EXERCISE:1到該整數的三角形數字數列
n = int(input("請輸入正整數:"))
for i in range(1, n+1):
    print()
    for j in range(1,i+1):
        print(j,end="")

break命令:
for i in range(1,11):
    if(i==6):
        break
    print(i, end=",")   #執行結果:1,2,3,4,5

continue迴圈: 在執行中途暫時停住不往下執行，而跳到迴圈起始處繼續執行
for i in range(1, 11):
    if(i==6):
        continue
    print(i, end=",")   #執行結果:1,2,3,4,5,7,8,9,10
EXERCISE:
n = int(input("請輸入大樓的樓層數:"))
print("本大樓具有的樓層為:",end="")
print()
for i in range(1, n+1):
    if(i==4):
        continue
    print(i, end=" ") 

while迴圈:
while(條件式):
    程式區塊
EXAMPLE:
total = n = 0
while(n < 10):
    n += 1
    total += n
print(total)  #1+2+....+10=55
EXERCISE:
n = int(input("請輸入正整數n的值:"))
num = 1
while(num <= n):
    if num % 2 == 0:
        print(num,end=' ')
    num += 1

EXERCISE:
sum = 0
for i in range(1, 100, 2):
    sum += i
print("1+3+5+...+99=",sum)

for i in range(2, 10):
    for j in range(2, 10):
        print('%d*%d=%d'%(i,j,i*j),end=" ")
    print()

n = int(input("請輸入正整數:"))
for i in range(n):
    for j in range(n-i):
        print('*',end="")
    print('\n',end="")

sum = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 7 == 0:
        sum += i
print("數值 1~100 中，所有是 3 或 7 倍數的數之總和 =",sum)

以下是辨認質數和列出因數的程式
calc=int(input("請輸入正整數:"))
data=str()
result=int(0)
for i in range(1,calc+1):
    res = calc % i
    if res == 0 :
        data=data+" "+str(i)
        result+=1
print(str(calc)+" 的因數有"+ data)
if result > 2:
    print(str(calc)+" 不是質數")
else:
    print(str(calc)+" 是質數")  
"""     