case=1
while True:
    try:
        K,L=map(int,input().split())
        if K<0 and L<0:
            break
        count=0
        subK,subL=K,L
        while True:
            count+=1
            if K==1:
                break
            if K%2==0:
                K/=2
                if K>L:
                    break
            elif K%2!=0:
                K=K*3+1
                if K>L:
                    break
        print("Case %d: K = %d, limit = %d, number of terms = %d"%(case,subK,subL,count))
        case+=1
    except EOFError:
        break