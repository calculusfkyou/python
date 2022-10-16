while(True) :
    date = input()
    month = int(date[4]+date[5])
    date2 = int(date[6]+date[7])
    if month >= 10 and month <= 12 and date2 % 2 != 0 :
        print("科學麵+飲料")
    elif month >= 10 and month <= 12 and date2 % 2 == 0 :
        print("科學麵")
    elif month <= 10 and date2 % 2 != 0 :
        print("飲料")
    else :
        print("0")