#10611128=10100001 11101001 10111000
#a1^a2=00 11101001 10 =233 前後兩個不要
#(b1^b3)^b2=11110000=240
#10811133=101001001111 011011111101
#a1^a2=11 00101100 10 =44
#10811217=101001001111
#a1^a2=   011101010001
def BtoD(num):
    temp=0
    bs=0
    while num>0:
        temp+=(num%10)*2**bs
        bs+=1
        num=num//10
    return temp
while True:
    try:
        A=int(input())
        ba,bs,t=0,0,0
        while A>0:
            ba+=(A%2)*10**bs
            bs+=1
            t+=1
            A=A//2
        Bt=t//3
        subt=t//3#for B1 B2 B3
        subba=ba#for B1 B2 B3
        a1,a2,bs=0,0,0
        if t%2==1:
            tt=t//2
            t=tt+1
            a1t,a2tt=t,tt
            while tt>1:#a2
                a2+=(ba%10)*10**bs
                tt=tt-1
                bs+=1
                ba=ba//10
            bs=0
            a1=ba#a1
        else:
            tt=t//2
            t=tt
            a1t,a2tt=t,tt
            while tt>0:#a2
                a2+=(ba%10)*10**bs
                tt=tt-1
                bs+=1
                ba=ba//10
            bs=0
            a1=ba
        a2=a2%(10**(a2tt-2))//100
        a1=a1%(10**(a1t-2))//100
        a2,a1=BtoD(a2),BtoD(a1)
        print(a1^a2,end=" ")
        temp,bs,b=0,0,[]
        while subba>0:
            for i in range(subt):
                temp+=(subba%10)*10**bs
                bs+=1
                subba=subba//10
            b.append(BtoD(temp))
            temp=0
            bs=0
        print((b[0]^b[2])^b[1])
    except EOFError:
        break