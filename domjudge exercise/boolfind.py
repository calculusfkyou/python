# def solve(num):
#     if num==1:
#         return 1
#     else:
#         return 0

# def main():   
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         temp=list(map(int,input().split()))
#         mid=int(n/2)
#         print("READ %d"%(mid))
#         while True:
#             if temp[mid]==0:
#                 print("READ %d"%(mid-1))
#                 if solve(temp[mid-1])==1:
#                     print("OUTPUT %d"%(mid-1))
#                     break
#                 mid-=1
#             if temp[mid]==1:
#                 print("READ %d"%(mid+1))
#                 if solve(temp[mid-1])==0:
#                     print("OUTPUT %d"%(mid+1))
#                     break
#                 else
#                 mid+=1
# main()

t = int(input())
for _ in range(t):
    n = int(input())
    lo, hi = 0, n-1
    while lo < hi:
        mid = (lo + hi) // 2
        print(f"READ {mid}")
        response = input().strip().lower()
        if response == "true":
            hi = mid
        else:
            lo = mid + 1
    print(f"OUTPUT {lo}")