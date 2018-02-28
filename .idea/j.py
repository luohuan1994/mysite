b=0
leap=1
for i in range(101,200,2):
    for j in range(2,i):
        if i%j == 0:
            leap=0
            break
    if leap == 1:
        print(i)
        b+=1
    leap=1
print('the total is %d' % b)
