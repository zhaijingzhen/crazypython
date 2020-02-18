#面向对象三大特征：封装（定义类的过程）、多态、继承

#多态   同一方法在不同的类中，有不同的功能
#数字类
#1+1
#字符串类
#'1'+'1'

class Triangle:
    def __init__(self,width,height):      #初始化
        self.width = width
        self.height = height
    def getArea(self):
        area = self.width * self.height /2
        return area

class Square:
    def __init__(self,size):      #初始化
        self.size = size
    def getArea(self):
        area = self.size * self.size
        return area
a = Triangle(6,8)
print(a.getArea())
b = Square(9)
print(b.getArea())

#以上代码实现了，getArea方法在两个不同的类中，使用了不同的方法，这就是多态


