import re,os
#text = "john ks handsome boy, he is cool,clever,and so on..."
#print(re.sub('\s+','-',text))
#p = re.compile(r'\d{3}-\d{6}')
#print(p.findall('010-628888'))
'''
def create_counter(n):
    print("create counter")
    while True:
        yield n
        print("increment n")
        n+=1
cnt = create_counter(2)
print(cnt)
print (next(cnt))
print(next(cnt))
'''
'''
def cube(n):
    for i in range(n):
        yield i ** 3
for i in cube(3):
    print(i)

s = 'hellobaby'
def findchar(s):
    for i in s:
        if s.count(i)==1:
            return i,s.index(i)
m,n=findchar(s)
print('第一个出现一次的字符是{}')
'''
def x(fun):
    def y():
        print (1)
    return y()
def f():
    print (2)

x(f())
