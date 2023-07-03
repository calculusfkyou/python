while True:
    try:
        n=int(input())
        nums=[]
        for i in range(n):
            nums.append(int(input()))
        lack=[]
        begin,end=nums[0],nums[-1]
        if begin!=1:
            for i in range(1,begin):
                lack.append(i)
        for i in range(begin,end):
            if i not in nums:
                lack.append(i)
        if len(lack)==0:
            print("good job")
        else:
            for i in lack:
                print(i)
    except EOFError:
        break