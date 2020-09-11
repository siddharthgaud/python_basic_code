thistuple = ("apple","banana","cherry")
print(thistuple)

thistuple = ("apple","banana","cherry")
print(thistuple[0])

thistuple = ("apple","banana","cherry")
print(thistuple[-3])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-4])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

thistuple= ("apple", "banana", "cherry")
if "applee" in thistuple:
    print("yes! apple is present in this tuple")
else:
    print("not present applee")

thistuple= ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

'''thistuple= ("apple", "banana", "cherry")
del thistuple'''

tuple1 = ("a","b","c")
tuple2 = (1,2,3)
tuple3 = tuple1 +tuple2
print(tuple3)

thistuple= tuple(("apple", "banana", "cherry"))
print(thistuple)
































































