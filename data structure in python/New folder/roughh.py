'''a = 0
b = 1
for i in range(10):
    print(a)
    a,b = b,a+b'''
'''a= 0
b = 1
c  = a+b
for i in range(2,10):
    print(a)
    a,b = b,a+b'''

'''a = 0
for i in range(10):
    if a %2 ==0:
         print(a)
    a +=1'''

'''a = 0
while a<20:
    if a %2 =0:
        print(a)
    a +=1'''

Number = 1

while (Number <= 20):
    count = 0
    i = 2

    while (i <= Number // 2):
        if (Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" % Number, end='  ')
    Number = Number + 1
    




