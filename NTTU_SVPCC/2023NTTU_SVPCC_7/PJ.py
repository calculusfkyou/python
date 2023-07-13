import random
def main():
    while True:
        try:
            c,e,m=map(int,input().split())
            ans=[]
            for i in range(2,m):
                if m%i==0:
                    if e==(i+m//i)*2:
                        ans.append([i+2,m//i+2])
            # print(ans)
            if len(ans)==0:
                print('impossible')
            else:
                print(*random.choice(ans))
        except EOFError:
            break
main()