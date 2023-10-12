# 建立矩形類別求矩形面積、三角形類別繼承矩形類別求三角形面積
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Rectangle):
    def area2(self):
        return super().area() / 2


rec = Rectangle(5, 6)
print('矩形面積=', rec.area())
tri = Triangle(5, 6)
print(tri.area())
print(tri.area2())
