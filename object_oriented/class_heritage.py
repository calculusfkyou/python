# 類別繼承
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def hello(self):
#         print("I'm " + self.name)
#
#
# class Son(Person):
#     # 覆寫父類別的建構式
#     def __init__(self, name):
#         self.name = 'son\'s name is ' + name
#
#     # 新增子類別的方法
#     def talk(self):
#         print(self.name + ' can say En too.')
#
#
# # 建立父類別物件
# person1 = Person('David')
# person1.hello()
# # 建立子類別物件
# son = Son('joe')
# son.hello()
# son.talk()


# 使用 super() 方法執行父類別的方法
class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(self.name + "說哈囉")


class Son(Person):
    # 覆寫父類別的建構式
    def __init__(self, name):
        super().__init__(name)  # 呼叫父類別的這個方法

    # 新增子類別的方法
    def talk(self):
        super().hello()
        print(self.name + "也會說英語")


# 建立父類別物件
person1 = Person("David")
person1.hello()
# 建立子類別物件
son = Son("joe")
son.talk()
