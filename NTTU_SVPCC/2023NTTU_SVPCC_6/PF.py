while True:
    try:
        t,s,n=map(int,input().split())
        times=list(map(int,input().split()))
        hourglass=[0,s]#[上,下]
        less=t-times[-1]
        record=0
        for i in range(len(times)-1):
            t=times[i+1]-times[i]
            if t<s:
                hourglass[0]=hourglass[1]-t
                hourglass[1]=s-hourglass[0]
            else:
                hourglass[0]=0
                hourglass[1]=s
        hourglass[0],hourglass[1]=hourglass[1],hourglass[0]
        if hourglass[0]<=less:
            print(0)
        else:
            print(hourglass[0]-less)
    except EOFError:
        break
#2000 333 3
# 1000 1250 1500

# 100 10 5
# 15 20 93 96 97