while True:
    try:
        s=input()
        if s=='':
            break
        for i in range(len(s)-1):
            print(s[i]+s[i+1:]+s[:i],end=" ")
        print(s[-1]+s[0:-1])
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