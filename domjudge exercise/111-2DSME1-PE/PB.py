while True:
    try:
        n=input()
        for i in range(0,len(n)-3,3):
            print(chr(int(n[i:i+3])),end="")
        print(chr(int(n[-3:])))
    except EOFError:
        break