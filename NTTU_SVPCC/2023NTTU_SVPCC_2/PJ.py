# 前綴和後綴和的應用    
while True:
    try:
        n=int(input())
        val=list(map(int,input().split()))
        prefix,suffix=[],[]
        for i in range(len(val)):
            prefix.append(sum(val[:i+1])/(i+1))
        for i in range(len(val),0,-1):
            suffix.append(sum(val[i-1:])/(len(val)-i+1))
        # print(prefix)
        # print(suffix)
        if max(prefix+suffix)>0:
            print("%.9f"%(max(prefix+suffix)))
        else:
            print("%.9f"%(0))
    except EOFError:
        break
# def main():
#     while True:
#         try:
#             n=int(input())
#             val=list(map(int, input().split()))
#             prefix_sum=[0]*(n + 1)
#             suffix_sum=[0]*(n + 1)
#             for i in range(n):
#                 prefix_sum[i+1]=prefix_sum[i] + val[i]
#             for i in range(n-1,-1,-1):
#                 suffix_sum[i]=suffix_sum[i+1] + val[i]
#             max_avg=0
#             for i in range(1,n+1):
#                 max_avg = max(max_avg,max(prefix_sum[i]/i,suffix_sum[i]/(n-i)))

#             if max_avg>0:
#                 print("%.9f"%max_avg)
#             else:
#                 print("%.9f"%0)
#         except EOFError:
#             break
# main()