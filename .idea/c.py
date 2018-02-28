'''
class people:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p=people('zhang',19,100000)
print(p.name)
print(p.age)
print(p._people__salary)

class A:
    def foo(self):
        print('from A foo')
        self.bar()
    def bar(self):
        print('from A bar')

class B(A):
    def bar(self):
        print('from B bar')

b=B()
b.foo()
'''

class people:
    def __init__(self,name,age,height,weight,hobby):
        self.__name=name
        self.__age=age
        self.__height=height
        self.__weight=weight
        self._hobby=hobby

    def tell_info(self):
        print('''
        name:%S
        age:%s
        height:%s
        weight:%s
        '''
        %(self.__name,self.__age,self.__height,self.__weight))

p=people('zhang',23,144,55,'swim')
p.tell_info()




















