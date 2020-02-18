#面向对象编程
'''
一些定义 OOP
面向过程 & 面向对象
python对象
1. 属性（对象的特征）
2. 方法（对象的操作）
点记法访问    a.func()
'''
#定义类
class Car:
    color = ''
    def run(self):
        print('go go go!')
#实例化类的一个对象
bmw = Car()
print(bmw)
#访问类的属性
bmw.color = 'red'
print(bmw.color)
#访问类的方法
bmw.run()

#类的属性
'''
公有属性   公有属性定义名称时，不带 __
大家都能用的类的属性
私有属性   __money = 8000         __名称
类的内部用来传值使用的是私有属性，外部无法访问该私有属性
公有方法   公有方法定义名称时，不带 __
私有方法   def __lie(self):       __名称
                print('I have 5000')
特殊方法   __init__()   #初始化对象
魔术方法   
'''
class Human:
    name = 'Mike'
    gender = 'male'
    age = '25'
    __money = 8000   #定义薪资为私有属性，默认值8000
    def __init__(self,name,gender,age):      #初始化对象用 __init__
        print('#'*30)
        self.name = name
        self.gender = gender
        self.age = age
        print('#'*30)
    
    def __str__(self):
        msg = 'hi! I am the object of the Human.'
        return msg

    def say(self):
        print("my name is %s and I have %d" %(self.name,self.__money))
        self.__lie()

    def __lie(self):
        print('I have 5000')    

    
'''
zhangsan = Human()
print(zhangsan.name)
print(id(zhangsan.name))
zhangsan.name = 'Bob'   #给类的属性重新赋值
print(zhangsan.name)
print(id(zhangsan.name))
# print(zhangsan.__money)   #无法访问，程序报错
zhangsan.say()
'''
zhangsan = Human('Libaoming','femal',76)
print(zhangsan)
print(zhangsan.name,zhangsan.gender,zhangsan.age)