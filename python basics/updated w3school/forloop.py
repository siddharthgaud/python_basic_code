fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
for x in "banana":
    print(x)

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple","banana","cherry"]            #print statement after the break
for x in fruits:

    if x == "banana":
        break
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
    print(x)

for c in range(23,50,3):
    print(c)

for x in range(10):
    print(x)
else:
    print("finally finished")

adc = ["fe","efef","ef2ef","efef"]
avf = ["e3f3","Ffe","ffeff","ffeff"]

for x in adc:
    for y in avf:
        print(x,y)

for x in [0,1,2,3]:
     pass

for letter in "efbcnexbcgyvcbegvhcvebxqnjxdvcnqyvc":
    print(len(letter))
    if letter == "e" or letter == "f":
        continue
    print(letter)


sum = 0
for i in range(1,50):
    sum = sum + i
print("sum of ten natural numbers :"+str(sum))







