class A:  # 類別名稱後的小括號是繼承用的，若無繼承，可省略

    # 建構式 def __init__(self) 小括號也可以有更多參數
    def __init__(self, name):
        print("init")
        self.name = name

    def hello(self):  # 要記得寫self，物件本身的意思
        print("hello")


# a = A("David")
# print(a.name)
# a.hello()

# 繼承
class B(A):  # B繼承A的類別，可以多重繼承，所以小括號可以有更多類別名稱
    pass


b = B("heritage")
print(b.name)


# 參數預設值
class Person:
    def __init__(self, name="david", age=30):
        self.name = name
        self.age = age

    def hello(self):
        print("I'm " + self.name)


p1 = Person()
p2 = Person("John")
print(p1.name, p1.age, p2.name)
p1.hello()
p2.hello()


# exercise 用類別求矩形面積
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rec = Rectangle(5, 6)
print("矩形面積 =", rec.area())
