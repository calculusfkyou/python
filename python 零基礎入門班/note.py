# 整數: int
# 浮點數: float
# 布林值: true, false
# 字串: str ('' or "")
# 換行: \n 單雙引號: \', \" 反斜線: \\
"""
資料型態轉換: int(), float(), str()
num1 = 15 + int("35")
score = 60 
print("小明的成績為" + str(score))

print(item1,... , sep=分隔字元, end=結束字元)
print(100, "我是帥哥", 60, sep="&")
print(100, 60, sep="&", end="")

print(項目 % (參數列)) #數字前負號是向左靠齊
%%: 顯示
%d: 整數 %f: 浮點數 %s: 字串 %e, %E: 科學記號
print('%20s %-20s' % ('Apple\'s Products:','iPhone'))
print('%-20d %20d' % (52,22))

print(字串.format(參數列)) 
print('Member {0:7s}, discount {1:3.2f}'.format('Karen', 0.35))

變數 = input([提示字串])
num1 = eval(input('Enter height:'))  #eval讓字串變為數值
score = input("請輸入成績": )
print(int(score) + 10)  # 沒用eval就要這樣寫 int 或 float 或 str

+, -, *, /
% 餘數 // 商數 
** 次方 2**3=8

== != <= >= < >

not, and, or
not(3>5)  True 
not(5>3)  False 
(5>3)and(9>6)  True
(5>3)and(9<6)  False
(5<3)and(9>6)  False
(5<3)and(9<6)  False
(5>3)and(9>6)  True
(5>3)and(9<6)  True
(5<3)and(9>6)  True
(5<3)and(9<6)  False

+=, -=, *=, /=, %=, //=, **=

#homework
name1 = (input("請輸入第一位學生的姓名:"))
num1 = eval(input("請輸入第一位學生的成績:"))
name2 = (input("請輸入第一位學生的姓名:"))
num2 = eval(input("請輸入第一位學生的成績:"))
num3 = num1 + num2
print('姓名   ','成績')
print(name1   ,num1)
print(name2   ,num2)
print('成績總分為:',num3)
"""
num1 = int(input("請輸入路成功公里數(整數):"))
num2 = (num1 - 1) * 30 + 70
print("你的車程車資費為:",num2)