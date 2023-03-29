while True:
    try:
        s=input()
        if s=='':
            break
        temp=[]
        for i in range(len(s)-1):
            if s[i]+s[i+1:]+s[:i] not in temp:
                print(s[i]+s[i+1:]+s[:i],end=" ")
            temp.append(s[i]+s[i+1:]+s[:i])
        if s[-1]+s[0:-1] not in temp:
            print(s[-1]+s[0:-1])
            temp.append(s[-1]+s[0:-1])
        temp.clear()
    except EOFError:
        break

# while True:
#     try:
#         s=input()
#         if s=='':
#             break
#         for i in range(len(s)):
#             rotated=s[i:]+s[:i]
#             print(rotated,end=' ')
#         print()
#     except EOFError:
#         break