# 多重繼承和多型
class Father:  # 定義父類別
    def say(self):  # 定義共用方法
        print("明天會更好!")


class Mother:  # 定義父類別
    def say(self):  # 定義共用方法
        print("包容、尊重!")


class Child(Mother, Father):  # 定義子類別
    # 若此類別無override，則會先檢查繼承的第一個類別有無此方法，若有則會執行，否則往後面繼承的類別繼續找尋。
    def say(self):  # 定義共用方法
        print("hello")


child = Child()  # 建立 child 物件
child.say()
