#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Access tuple item
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Check if item exist
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))






















































