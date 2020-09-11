#while statement
'''count = 0
while count<3:
    count = count +1
    print("siddharth")'''
#while else statement
'''count = 0
while count<3:
    count = count +1
    print("siddharth")
else:
    print("while else block")'''
#for loop statement
'''numbers = [10,20,30,40,50]
sum = 0
for val in numbers:
    sum = sum +val
print("sum is ",sum)'''
#for loop with else
'''digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")'''
#types of loops
'''print("list of iterations :")
l = ['geeks','for','geeks']
for i in l:
    print(i)
print("\ntuple iterations :")
t = ('python','is','awesome')
for i in t:
    print(i)
print("\n string iterations")
s = 'python'
for i in s:
    print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i])) '''
#challenge
num = int(input("enter the number of rows:"))
for i in range(0,num+1):
    for j in range(0,i+1):
        j = j + 1
    i = i+1
    print(i,end=" ")
    print(j)


