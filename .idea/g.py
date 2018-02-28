class MyTest:
    myname='peter'
    def __init__(self,name):
        self.name=name
    def sayhello(self):
        print("say hello to %s" % self.name)
    def sayhello_1(self):
        print("say hello to %s" % self.myname)
    def sayhello_2(self):
        print("say hello to %s" % self.name)
    def sayhello_3(self):
        # print ("say hello to %s" % MyTest.name)
        pass

if __name__=='__main__':
    test = MyTest("abc")
    test.sayhello()
    test.sayhello_1()
    test.sayhello_2()
    test.sayhello_3()

    MyTest.yourname="Allen"
    print(MyTest.myname)
    print(MyTest.yourname)
