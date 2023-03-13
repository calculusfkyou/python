n=int(input())
for i in range(n):
    num=input()
    if num=="Inf":
        print("%.6f"%(0))
    elif num=="-Inf":
        print("%.6f"%(-0))
    elif num=="+0":
        print("inf")
    elif num=="-0":
        print("-inf")
    elif num=="nan":
        print("NaN")
    else:
        num = float(num)
        if num == 0:
            print("%.6f"%(0))
        else:
            print("%.6f"%(1/num))