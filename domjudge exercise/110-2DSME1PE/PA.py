def Sierpinski(val):
    if val==1:
        return 1
    elif val!=1:
        return 3**(val-2)*4+Sierpinski(val-1)

n=int(input())
sub=n
temp=0
if n==1:
    print("1")
    print("1")
else:
    print(Sierpinski(n))
    for i in range(n):
        temp+=Sierpinski(sub)
        sub-=1
    print(temp)