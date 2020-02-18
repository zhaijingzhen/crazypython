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
Tom = Father()
print(Tom.money1)
Tom.drive()

print('#'*50)
Jerry = Son()
print(Jerry.money1)
Jerry.drive()
Jerry.pay()
print(Jerry.money2)