"""
import math
while True:
    f = eval(input())
    a = int(math.log(abs(f),2))
    print(a)
"""
"""
import math
while True:
    f = eval(input())
    a = int(math.log(abs(f),2))
    Fm = abs(f) / (2**a) - 1
    for i in range(1,24):
        value = (int(Fm * 2),(Fm * 2)%1)
        Fm=value[1]
        print(value[0],end="")
    print(end="")
    print()
"""
"""
import math
while True:
    f = eval(input())
    a = int(math.log(abs(f),2))
    b = a + 127
    c=0
    if f > 0:
        print(0,end="")
    else:
        print(1,end="")
    if a < -127:
        c=b
        b = 0
    getbinary = lambda x, n: format(x, 'b').zfill(n)
    print(getbinary(b, 8),end="")
    Fm = ((abs(f) / (2**(a-c)) )*(2**c))%1
    for i in range(1,24):
        value = (int(Fm * 2),(Fm * 2)%1)
        Fm=value[1]
        print(value[0],end="")      
    print(end="")
    print()
"""