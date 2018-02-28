'''
class Foo(object):
    def hi(self):
        print("hi,Foo")

class Foo2(Foo):
    def hi(self):
        super(Foo2,self).hi()

if __name__=='__main__':
    foo2 = Foo2()
    foo2.hi()

class Foo(object):
    val =0
    def __init__(self):
        self.val=1

if __name__=='__main__':
    foo=Foo()
    print(foo.val)
    print(Foo.val)
'''
class Foo(object):
    def __init__(self):
        self.val=1
