thislist = ["apple","mango","cherry"]
print(thislist)

thislist = ["apple","mango","cherry"]
print(thislist[1])

thislist = ["apple","mango","cherry"]
print(thislist[-1])

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelo","grapes"]
print(thislist[2:5])

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelo","grapes"]
print(thislist[:5])

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelo","grapes"]
print(thislist[2:])

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelo","grapes"]
print(thislist[:])

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
print(thislist[-4:-1])

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist[1] = "balckcurrent"
print(thislist)

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
for x in thislist:
    print(x)

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
if "potato" in thislist:
    print("yes apple in this list")
else:
    print("not in this list")

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
print(len(thislist))

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist.append("potato")
print(thislist)

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist.insert(2,"holol")
print(thislist)

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist.remove("grapes")
print(thislist)

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist.pop(1)
print(thislist)        #del keyword is same as pop

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
del thislist[1]
print(thislist)

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist.clear()
print(thislist)

thislist = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
mylist = thislist.copy()
print(mylist)

thislist1 = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist2 = ["appleee","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist3 = thislist1 + thislist2
print(thislist3)

thislist1 = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist2 = ["appleee","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
for x in thislist2:
    thislist1.append(x)
print(thislist1)

thislist1 = ["apple","mango","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist2 = ["appleee","mangooo","cherry","kiwi","banana","orange","watermelon","grapes"]
thislist1.extend(thislist2)
print(thislist1)

thislist1 = list(["app&&&le","mango","cherry","kiwi","banana","orange","watermelon","grapes"])
print(thislist1)

a = [1,2,3]
b = [1.5,2,a]
print(b)

x= range(1,4)
print(x[1])
print(len(x))

print(len(a))

a = [1,2,3,4]
b = [5,6]
print(a+b)
print(a*3)

x= range(10)
print(x)

a= [1,2]
a.append(3)
print(a)

x = [0, 1, [2]]
x[2][0] = 3
print(x)
