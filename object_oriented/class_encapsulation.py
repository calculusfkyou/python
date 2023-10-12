# 類別封裝
# 屬性或方法前面加上__就會封裝成private，只有類別內部可以使用
# 若有其他類別繼承此類別，private的屬性或方法將不會被繼承
class Bank:
    def __init__(self, money):
        self.__money = money  # 總存款 屬性前面加上兩個底線就變成private

    def __show(self):  # 顯示總存款 方法名稱前面加上兩個底線就變成private
        return self.__money

    # def save(self, amount):  # 存款
    #     self.money += amount
    #
    # def fetch(self, amount):  # 提款
    #     self.money -= amount


b = Bank(1000)
b.__money = 20000
# b.__show()
