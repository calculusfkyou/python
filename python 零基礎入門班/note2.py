"""
a = eval(input("請輸入年齡:"))
if a < 6 : 
    print("可看普遍級!")
elif a >= 6 and a < 12 : 
    print("可看普遍級及保保護級!")
elif a >= 12 and a <18 : 
    print("可看限制級以外的所有影片!")
elif a >=18 : 
    print("您已成年，可看各級影片!")

a = eval(input("請輸入a的值:"))
b = eval(input("請輸入b的值:"))
c = eval(input("請輸入c的值:"))
if a > b and a > c :
    print("最大值為",a)
elif b > a and b > c :
    print("最大值為",b)
elif c > a and c > b :
    print("最大值為",c)

a = input("今天會下雨嗎?")
if "y" in a :
    print("出門記得帶傘!")
else :
    print("")

a = eval(input("請輸入正整數:"))
if a % 2 == 0 : 
    print(a,"為偶數!")
else :
    print(a,"為奇數!")

a = eval(input("請輸入月份:"))
if a >= 1 and a <=3 :
    print(a,"月是春天!")
elif a >=4 and a <= 6 :
    print(a,"月是夏天!")
elif a >=7 and a <= 9 :
    print(a,"月是秋天!")
elif a >=10 and a <= 12 :
    print(a,"月是冬天!")    
else :
    print(a,"月份不再範圍內!")
"""
a = eval(input("請輸入今年收入淨額:"))
if a >= 2000000 :
    print('%s %2f元'%("付稅金額:",a*0.3))
elif a <= 1999999 and a >=1000000 :
    print('%s %2f元'%("付稅金額:",a*0.21))
elif a <= 999999 and a >= 600000 :
    print('%s %2f元'%("付稅金額:",a*0.13))
elif a <= 599999 and a >= 300000 :
    print('%s %2f元'%("付稅金額:",a*0.06))
elif a <= 299999 :
    print('%s %2f元'%("付稅金額:",0))