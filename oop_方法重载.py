#方法重载
#在子类中重新定义父类的方法，就是方法重载
#同时可以直接调用父类的方法，互不影响

class Father:
    money1 = '1000000'
    __money = '100000000'
    def drive(self):
        print('I can drive a car.')
class Mother:
    money2 = '9999999'
class Son(Father,Mother):
    def pay(self):
        print(self.money1)
    def drive(self):
        print('I can drive a tank!')
        Father.drive(self)
Tom = Father()
print(Tom.money1)
Tom.drive()

print('#'*50)
Jerry = Son()
print(Jerry.money1)
Jerry.drive()
Jerry.pay()
print(Jerry.money2)