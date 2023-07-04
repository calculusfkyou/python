while True:
    try:
        n=int(input())
        subn=n
        if n==1:
            print("HAPPY")
        else:
            check=0
            while n!=1:
                record=0
                while n>0:
                    record=record+((n%10)**2)
                    n=n//10
                n=record
                # print(record)
                if n==1:
                    print("HAPPY")
                    check=1
                    break
                elif n==4 or n==16 or n==37 or n==58 or n==89 or n==145 or n==42 or n==20:
                    print("UNHAPPY")
                    break
    except EOFError:
        break