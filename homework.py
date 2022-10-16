"""
print('%20s %-20s' % ('Apple\'s Products:','iPhone'))
print('%20s %-20s' % ('','iMac'))
print('%20s %-20s' % ('','...'))

print('Member {0:7s}, discount {1:3.2f}'.format('Karen', 0.35))
print('Member {0:7s}, discount {1:3.2f}'.format('Sammy', 0.4))
print('Member {0:7s}, discount {1:3.2f}'.format('JoJo', 0.42))

print('%20s %-20s' %('tall', 'short'))
print('%20s %-20s' %('strong', 'weak'))
print('%20s %-20s' %('thick', 'thin'))

print('%-15s %7s'% ('City', 'Celsius'))
print('%-15s %7.2f' % ('Taipei', 33.2))
print('%-15s %7.2f' % ('Yilan', 32.93))
print('%-15s %7.2f' % ('MiaoLi', 32.29))
print('%-15s %7.2f' % ('Taichung', 32.48))
print('%-15s %7.2f' % ('HuaLian', 33.87))

print('|%6d %6d %6d %6d|' % (22, 44, 66, 88))
print('|%-6d %-6d %-6d %-6d|' % (33, 55, 77, 99))
print('|%6d %6d %6d %6d|' % (222, 444, 666, 888))
print('|%-6d %-6d %-6d %-6d|' % (333, 555, 777, 999))

print('---------')
print('Learning Python now', end = '***')
print('')
print('Python is fun$$$')
print('---------')

num1, num2, num3, num4, num5 = eval(input ('Enter five numbers separated by commas:'))
sum = num1 + num2 + num3 + num4 + num5
average = sum / 5
print('Sum = %d \nAverage = %.2f'%(sum, average))

num1 = eval(input('Enter height:'))
num2 = eval(input('Enter weight:'))
Height = num1
Weight = num2
Perimeter = (num1 + num2)*2
Area = num1 * num2
print('Height = %.2f\n Weight = %.2f\n Perimeter = %.2f\n Area = %.2f'%(Height, Weight, Perimeter, Area))

s = eval(input('Enter the side length of the positive triangle:'))
Height = (3**0.5)/2*s  
Area = (3**0.5)/4*(s**2)
print('Height = %.2f\nArea = %.2f'%(Height, Area))

x = eval(input('Enter x(min)=')) 
y = eval(input('Enter y(sec)='))
z = eval(input('Enter z(km)='))
Speed = (z/1.6)/(x/60 + y/3600)
print('Speed = %.1f miles/hour'%(Speed))

import math
n = eval(input('請輸入邊數:'))
s = eval(input('請輸入邊長:'))
area = (n * s *s )/(4 * math.tan(math.pi/n))
print('Area = %f'%(area))

import math
x1 = eval(input('請輸入x座標:'))
y1 = eval(input('請輸入y座標:'))
x2 = eval(input('請輸入x座標:'))
y2 = eval(input('請輸入y座標:'))
distance = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
print('Distance = %f'%(distance))

a, b, c = eval(input('Enter the side length of the triangle separated by commas:'))
s = (a + b + c)/2
area = pow(s* (s-a)* (s-b)* (s-c), 0.5)
print('Area = %f'%(area))

a, b, c = eval(input('Enter a , b , c separated by commas:'))
ans1 = (-b + b**2 - 4*a*c)/(2*a)
ans2 = (-b - b**2 - 4*a*c)/(2*a)
print('ans1 = %f\n ans2 = %f'%(ans1, ans2))

import math
x1, y1 = eval(input('Enter point1(latitude and longtitude) in degress:'))
x2, y2 = eval(input('Enter point2(latitude and longtitude) in degress:'))
d = 6371.01 * math.acos(math.sin(x1)* math.sin(x2) + math.cos(x1)* math.cos(x2)* math.cos(y1-y2))
print('The distance between the points is %f km'%(d))

num = eval(input('請輸入購物金額:'))
if num >= 5000 and num <15000:
    print('You need to pay', format(num *0.95, '.1f'))
elif num >=15000 and num < 25000 :
    print('You need to pay', format(num *0.9, '.1f'))
elif num >=25000 and num < 35000 :
    print('You need to pay', format(num *0.85, '.1f'))
elif num >=35000 :
    print('You need to pay', format(num *0.8, '.1f'))
print('Enjoy shopping!')

month = eval(input('Enter a month:'))
if month >= 1 and month <=3:
    print(month, ' is spring')
elif month >= 4 and month <=6:
    print(month, ' is summer')
elif month >= 7 and month <=9:
    print(month, ' is autumn')
elif month >= 10 and month <=12:
    print(month, ' is winter')
elif month <1 and month >12:
    print(month, 'is not in season')

age = eval(input('Enter your age:'))
if age >=0 and age <=5:
    print('The ticket fee is free')
elif age >=6 and age<=11:
    print('The ticket fee is $590')
elif age >=12 and age<=17:
    print('The ticket fee is $790')
elif age >=18 and age<=59:
    print('The ticket fee is $890')
elif age >=60:
    print('The ticket fee is $399')

num = eval(input('Enter an integer:'))
if num % 3 == 0 and num % 15 != 0 :
    print('This number is multiples of three')
elif num % 5 == 0 and num % 15 != 0 :
    print('This number is multiples of five')
elif num % 15 == 0 :
    print('This number is multiples of three and five')

str = input('Enter an character:')
if  str.islower():
    print('This char is a lowercase letter')
elif str.isupper():
    print('This char is an uppercase letter')
elif str.isdigit():
    print('This char is a number')
else :
    print('This char is a special symbol')

num = eval(input('Enter your net income:'))
if num >=0 and num <=540000:
    num = num * 0.05 - 0
    print('Your tax Payable:', format(num,'.2f'))
elif num >=540001 and num <=1210000:
    num = num * 0.12 - 37800
    print('Your tax Payable:', format(num,'.2f'))
elif num >=1210001 and num <=24240000:
    num = num * 0.2 - 134600
    print('Your tax Payable:', format(num,'.2f'))
elif num >=2420001 and num <=4530000:
    num = num * 0.3 - 37600
    print('Your tax Payable:', format(num,'.2f'))
elif num >=4530001 and num <=10310000:
    num = num * 0.4 - 829600
    print('Your tax Payable:', format(num,'.2f'))
elif num >=10310001 :
    num = num * 0.45 - 1345100
    print('Your tax Payable:', format(num,'.2f'))

x = eval(input('Enter x:'))
y = eval(input('Enter y:'))
if (x**2 + y**2)**0.5 <=10 :
    print('This point is in this circle which radius is 10 and the center is (0,0)')
else : 
    (x**2 + y**2)**0.5 > 10 
    print('This point is not in this circle which radius is 10 and the center is (0,0)')

import random
evenCount = 0
oddCount = 0
numberCount = 0
for i in range (1,101):
    randomNumber = random.randint(1,100)
    numberCount += 1
    if numberCount % 10 ==0:
        print(format(randomNumber,'5d'))
    else:
        print(format(randomNumber,'5d'),end="")
    if randomNumber % 2 ==0:
        evenCount += 1 
oddCount = 100 - evenCount 
print('\nEven number:',evenCount,'\nOdd number:',oddCount)

total = 0
for i in range(1,101):
    if i % 3 == 0:
        total += i
print('3+6+...+99 =',total)

for i in range(1,10):
    for j in range(1,10):
        print('%5d'%(i*j),end=' ')
    print()

n = int(input('Enter the value of n: '))
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()

n = int(input('Enter the value of n: '))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end='')
    print()

for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%2d'%(j,i,i*j),end=' ')
    print()
 
sum = 0
for i in range (1,97,2):
    sum += i/(i+2)  
print(sum)
        
k = eval(input('How many workers are there:')) 
s = eval(input('Enter sales amount:'))
if s >= 0.01 and s < 5000:
    s = k*6000 + s*0.1
    print('Your salaries are %.2f'%(s))
elif s >= 5000 and s <= 10000:
    s = k*6000 + s*0.12
    print('Your salaries are %.2f'%(s))
elif s >= 10000 and s < 15000:
    s = k*6000 + s*0.14
    print('Your salaries are %.2f'%(s))
elif s >= 15000:
    s = k*6000 + s*0.16
    print('Your salaries are %.2f'%(s))

def gcdFunction(n1,n2):
    gcd = 1
    k = 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1
    return gcd

def main():
    number1 = eval(input('Please input an integer:'))
    number2 = eval(input('Please input an integer:'))
    answer = gcdFunction(number1,number2)
    print('The GCD for',number1,'and',number2,'is',answer)

main()
"""      
while (True):
    try:
        a=int(input())
        if (a%4==0 and a%100!=0) or a%400==0:
            print('閏年')
        else:
            print('平年')
    except EOFError:
        break

