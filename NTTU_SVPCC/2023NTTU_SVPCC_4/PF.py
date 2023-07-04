while True:
    try:
        n=int(input())
        predict,final=[],[]
        for i in range(n):
            predict.append([input(),i+1])
        for i in range(n):
            final.append([input(),i+1])
        # print(predict,final)
        diff=[]#[名字,最終,最終-預測]
        for i in range(len(predict)):
            for j in range(len(final)):
                if final[j][0]==predict[i][0]:
                    diff.append([predict[i][0],final[j][1],predict[i][1]-final[j][1]])
        check=0
        diff.sort(key=lambda diff:diff[1],reverse=1)
        diff.sort(key=lambda diff:diff[2])
        # print(diff)
        for i in range(len(diff)):
            if diff[i][2]<=0:
                check+=1
        if check==n:
            print("suspicious")
        else:
            print(diff[-1][0])
    except EOFError:
        break