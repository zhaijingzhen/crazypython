'''
闭包  函数式编程中的一个非常重要的语法结构

创建闭包
1. 闭包函数必须有内嵌函数
2. 内嵌函数需要引用该嵌套函数上一级函数的参数
3. 闭包函数必须返回内嵌函数
'''
def hello_conf(prefix):
    def hello(name):
        print(prefix,name)
    return hello

a = hello_conf('Good Morning!')
a('milo')

