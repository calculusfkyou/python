#找最小質因數
"""
def main():
    maxP = 1000000
    primeList = [True]*maxP
    for i in range(2,int((maxP-1)**0.5+1)):
        if primeList[i] == True :
            primeList[i] = i
            for j in range(i*i,maxP,i):
                if primeList[j] == True:
                    primeList[j] = i
    while True:
        list1 = list(map(int,input().split()))
        for i in range(0,len(list1)):
            if primeList[list1[i]] == True:
                list1[i] = list1[i]
            else:
                list1[i] = primeList[list1[i]]
        print(" ".join(str(i) for i in list1))
        #print(primeList)
main()
"""
"""
maxP = 10000000
primeList = [True]*maxP
for i in range(2,int((maxP-1)**0.5)):
    if primeList[i]:
        for j in range(i*i,maxP,i):
            primeList[j] = False
for i in range(2,maxP):
    if primeList[i]:
        print(i,end=" ") 
""" 
#質因數分解:           
"""
while True:   
    n=int(input())
    print(n,end="=")
    for k in range(2,n+1):
        while n!=k:
            if n%k==0:
                print(k,end="*")
                n=n/k
            elif n > 10000000:
                print("")
            else:
                break
    print(int(n)) 
"""               
#算有幾個因數:
"""
while True:
    calc=int(input())
    data=[]
    for i in range(1,calc+1):
        res = calc % i
        if res == 0 :
            data.append(i)
        if calc > 10000000:
            break
    print(len(data))
"""