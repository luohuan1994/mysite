class People:
    def __init__(self,name,age,height,weight,hobby):
        self.__name=name
        self.__age=age
        self.__height=height
        self._weight=weight
        self.hobby=hobby
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new):
        if not isinstance(new,str):
            raise TypeError('名字必须是字符串类型')
        self.__name=new
    @name.deleter
    def name(self):
        del self.name

p=People('lala',16,145,55,'read')
print(p.name)
p.name='ddd'
print(p.name)
del p.name
print(p.name)