def find_power_of_two(num):
    power=0
    while num>1:
        num=num/2
        power+=1
    return power
while True:
    try:
        n,k=map(int,input().split())
        field=[]
        if n==1:
            if k==1:
                print("1 1")
            elif k==2:
                print("1 2")
            elif k==3:
                print("2 2")
            elif k==4:
                print("2 1")
        else:
            if k==1:
                print("1 1")
            else:
                quadrant=1    #左下1 左上2 右上3 右下4
                subn,subk=n,k
                range=[0,0,0,0] #[x1,x2,y1,y2]
                check=0
                while subn!=1:
                    temp=[]
                    if subk<=(subn**2)//4:
                        if check:
                            range[1]-=subn//2
                            range[3]-=subn//2
                            range[0],range[1],range[2],range[3]=range[2],range[3],range[0],range[1]
                        else:
                            range=[1,subn//2,1,subn//2]
                            check=1
                        # if subk>((subn**2)//16) and subk<((subn**2)//16*2+1):
                        #     quadrant=2
                        # elif subk>((subn**2)//16*3) and subk<((subn**2)//4+1):
                        #     quadrant=4
                        # else:
                        quadrant=1
                    elif subk>(subn**2)//4 and subk<=(subn**2)//4*2:
                        if check:
                            range[1]-=subn//2
                            range[2]+=subn//2
                        else:
                            range=[1,subn//2,subn//2+1,subn]
                            check=1
                        subk=subk-(subn**2)//4
                        quadrant=2
                    elif subk>(subn**2)//4*2 and subk<=(subn**2)//4*3:
                        if check:
                            range[0]+=subn//2
                            range[2]+=subn//2
                        else:
                            range=[subn//2+1,subn,subn//2+1,subn]
                            check=1
                        subk=subk-(subn**2)//4*2
                        quadrant=3
                    elif subk>(subn**2)//4*3 and subk<=(subn**2):
                        if check:
                            range[0]+=subn//2
                            range[3]-=subn//2
                            tt=subn
                            for i in range(subn//2):
                                temp.append(tt)
                                temp.append(tt-2)
                                tt-=6
                            if subk not in temp:
                                range[0],range[1],range[2],range[3]=range[2],range[3],range[0],range[1]
                        else:
                            range=[subn//2+1,subn,1,subn//2]
                            check=1
                        subk=subk-(subn**2)//4*3
                        # if subk>((subn**2)//4*3) and subk<((subn**2)//16*13+1):
                        #     quadrant=1
                        # elif subk>((subn**2)//16*14) and subk<((subn**2)+1):
                        #     quadrant=3
                        # else:
                        quadrant=4
                    subn=subn//2
                    # print(quadrant)
                    # if quadrant==1:
                    #     if subk==2:
                    #         subk=4
                    #     elif subk==4:
                    #         subk=2
                    # elif quadrant==4:
                    #     if subk==1:
                    #         subk=4
                    #     elif subk==3:
                    #         subk=2
                    print(range)
                    # print(subk)
                # print(range[0],range[2])
    except EOFError:
        break