class Foo:
    def __init__(self,name):
        self.name=name
    def hi(self):
        print(self.name)
    @staticmethod
    def add(a,b):
        print(a+b)

if __name__=='__main__':
    foo01=Foo('letian')
    foo01.hi()
    foo01.add(1,2)
    Foo.add(1,2)